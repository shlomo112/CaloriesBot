from fastapi import Depends

from .services.whatsapp import WhatsAppHandler
from .services.llm_service import LLMService
from .services.calories_service import CaloriesService


def get_whatsapp_handler():
    return WhatsAppHandler()


def get_llm_service():
    return LLMService()


def get_calories_service(llm_service: LLMService = Depends(get_llm_service)):
    return CaloriesService(llm_service)
