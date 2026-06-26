
class WhatsAppHandler:

    def extract_message(self, payload: dict):
        try:
            data = payload["entry"][0]["changes"][0]["value"]
            messages = data.get("messages")

            if not messages:
                return None

            message = messages[0]
            if message["type"] != "text":
                return None

            return {
                "phone_number": message["from"],
                "message": message["text"]["body"]
            }

        except (KeyError, IndexError):
            return None
