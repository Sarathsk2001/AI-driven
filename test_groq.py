from litellm import completion
from dotenv import load_dotenv

load_dotenv(override=True)

response = completion(
    model="groq/llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "Say hello"}],
)

print(response.choices[0].message.content)

