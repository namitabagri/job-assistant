import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set")

if not OPENAI_MODEL:
    raise ValueError("OPENAI_MODEL is not set")

print(f"@@@@@@@@@@@@@@@@@@@@@@@@\nOPENAI_API_KEY: {OPENAI_API_KEY[:4]}...{OPENAI_API_KEY[-4:]}")  # Print only the first 4 characters for security
print(f"OPENAI_MODEL: {OPENAI_MODEL}\n@@@@@@@@@@@@@@@@@@@@@@@@")