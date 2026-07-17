from ..clients.openai_client import OpenAIClient


class LLMService:

    def __init__(self, openai_client: OpenAIClient) -> None:
        self.openai_llm = openai_client

    async def ask(self, system_prompt, user_prompt):

        return await self.openai_llm.chat(system_prompt, user_prompt)
