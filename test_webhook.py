import urllib.request
import json

data = {
    "object": "whatsapp_business_account",
    "entry": [{
        "changes": [{
            "value": {
                "messages": [{
                    "from": "972503920297",
                    "text": {"body": "סיננתי את השמן"},
                    "type": "text"
                }]
            }
        }]
    }]
}

encoded = json.dumps(data).encode()
req = urllib.request.Request(
    "http://localhost:8000/webhook",
    data=encoded,
    headers={"Content-Type": "application/json"},
    method="POST"
)
response = urllib.request.urlopen(req)
print(response.read())
