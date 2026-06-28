from ..clients import openai_client


class LLMService:

    def __init__(self, openai_client: openai_client.OpenAIClient) -> None:
        self.openai_llm = openai_client

    async def ask(self, system_prompt, user_prompt):

        return await self.openai_llm.chat(system_prompt, user_prompt)
