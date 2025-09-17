import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
# Load environment variables
load_dotenv()

# Configure LLM
def get_llm_global():
    return init_chat_model(
        "gpt-4o",
        model_provider="openai",
        temperature=0,
    )
