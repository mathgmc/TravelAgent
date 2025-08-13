from langchain.chat_models import init_chat_model
from settings.envs import LLM_OPENAI_MODEL, LLM_PROVIDER_GLOBAL, LLM_TEMPERATURE_PRECISE


# Configure LLM
def get_llm_global():
    return init_chat_model(
        LLM_OPENAI_MODEL,
        model_provider=LLM_PROVIDER_GLOBAL,
        temperature=LLM_TEMPERATURE_PRECISE,
    )
