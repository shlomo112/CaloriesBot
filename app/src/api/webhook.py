from fastapi import APIRouter, Request, Response, Query, Depends
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv

from app.src.services.whatsapp import WhatsAppHandler
from ..dependencies import get_calories_service, get_whatsapp_handler
import os

load_dotenv()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

router = APIRouter()


@router.get("/webhook")
async def verify_webhook_test(hub_mode: str = Query(alias="hub.mode"),
                              hub_verify_token: str = Query(
                                  alias="hub.verify_token"),
                              hub_challenge: str = Query(alias="hub.challenge")
                              ):
    """ callde by Meta when click verify and save on Meta cloud dashboard"""

    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:

        return PlainTextResponse(content=hub_challenge)

    return PlainTextResponse(content="Forbidden", status_code=403)


@router.post("/webhook")
async def receive_message(
    request: Request,
    whatsapp: WhatsAppHandler = Depends(
        get_whatsapp_handler),
    calories_service=Depends(get_calories_service)
):
    """called  by Meta whenever a whatsapp event occurs"""

    payload = await request.json()

    message = whatsapp.extract_message(payload)

    if message:
        response = await calories_service.process(
            phone=message["phone_number"],
            text=message["message"]
        )

        print(response)
        return {"response": response}

    return Response(status_code=200)
