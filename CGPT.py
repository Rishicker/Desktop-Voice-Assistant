import openai
import time

openai.api_key = "YOUR_API_KEY"

def generate_response(query):
    response = openai.Completion.create(
        engine="davinci",
        prompt=query,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message