from fastapi import Depends
import os

from .services.whatsapp import WhatsAppHandler
from .services.llm_service import LLMService
from .services.calories_service import CaloriesService
from .clients.openai_client import OpenAIClient


def get_whatsapp_handler():
    return WhatsAppHandler()


def get_openai_client():
    return OpenAIClient(api_key=os.getenv("OPENAI_API_KEY"))


def get_llm_service(openai_client: OpenAIClient = Depends(get_openai_client)):
    return LLMService(openai_client)


def get_calories_service(llm_service: LLMService = Depends(get_llm_service)):
    return CaloriesService(llm_service)
