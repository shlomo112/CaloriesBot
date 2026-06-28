from openai import APIStatusError, AsyncOpenAI


class OpenAIClient:
    def __init__(self, api_key) -> None:

        self.client = AsyncOpenAI(api_key=api_key)

    async def chat(self, system_prompt, user_prompt):
        try:
            response = await self.client.responses.create(
                model="gpt-5-mini",
                input=[
                    {"role": "system",
                     "content": system_prompt
                     },

                    {"role": "user",
                     "content": user_prompt
                     }
                ]
            )
            return response.output_text

        except APIStatusError as exc:
            raise exc
