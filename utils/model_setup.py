import os
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel, AsyncOpenAI

load_dotenv(override=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")

gemini_client = AsyncOpenAI(
    api_key = GEMINI_API_KEY,
    base_url = GEMINI_BASE_URL
)

gemini_model = OpenAIChatCompletionsModel(
    model = 'gemini-2.5-flash',
    openai_client = gemini_client
)