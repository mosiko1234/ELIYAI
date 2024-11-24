import openai

class OpenAIClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_document(self, prompt: str):
        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=1500
        )
        return response['choices'][0]['text']
