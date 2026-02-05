from dotenv import load_dotenv
import os

load_dotenv(override=True)

key = os.getenv("GROQ_API_KEY")

print("Key loaded:", key[:6] + "..." + key[-4:])
print("Length:", len(key) if key else None)

