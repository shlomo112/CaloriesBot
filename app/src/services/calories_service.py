from .llm_service import LLMService


class CaloriesService:
    def __init__(self, llm_service: LLMService) -> None:
        self.llm = llm_service

    async def process(self, phone: str, text: str):
        system_prompt = """
        You are a nutrition assistant.
        Your goal is to estimate calories as accurately as possible.

        Rules:
        1. If the food description is clear enough,
        provide a calorie breakdown per item and a total.

        2. If some information is missing but a reasonable estimate is possible,
        provide the estimate and clearly mention your assumptions.

        3. If the information is too vague, ask the user
        to be specific instead of guessing.

        Always reply in the same language the user wrote in.
        Keep responses concise and in plain text only — no markdown,
        no bold, no bullet symbols — because replies are sent via WhatsApp.
        """

        response = await self.llm.ask(system_prompt=system_prompt, user_prompt=text)

        return response

    def parse_food(self):
        pass
