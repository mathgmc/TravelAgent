import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# LLM Configuration
LLM_PROVIDER_GLOBAL = os.getenv("LLM_PROVIDER_GLOBAL", "openai")
LLM_OPENAI_MODEL = os.getenv("LLM_OPENAI_MODEL", "gpt-4o")
LLM_TEMPERATURE_PRECISE = os.getenv("LLM_TEMPERATURE_PRECISE", 0)

# MySQL DB
DATABASE_URL = os.getenv(
    "DATABASE_URL", "mysql+pymysql://myuser:mypassword@localhost:3306/mydb"
)
READ_DATABASE_URL = os.getenv(
    "READ_DATABASE_URL", "mysql+pymysql://myuser:mypassword@localhost:3306/mydb"
)

# SQS
SQS_ENDPOINT = os.getenv("SQS_ENDPOINT", "http://localhost:9324")
SQS_REGION = os.getenv("SQS_REGION", "us-east-1")
SQS_ACCESS_KEY = os.getenv("SQS_ACCESS_KEY", "x")
SQS_SECRET_KEY = os.getenv("SQS_SECRET_KEY", "x")
AGENT_QUESTION_QUEUE = os.getenv(
    "AGENT_QUESTION_QUEUE", "agent-question-queue"
)
AGENT_ANSWER_QUEUE = os.getenv(
    "AGENT_ANSWER_QUEUE", "agent-answer-queue"
)
