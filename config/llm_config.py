"""
LLM Configuration for AutoGen
"""
import os
from dotenv import load_dotenv

load_dotenv()

# GPT Configuration
gpt_config = {
    "model": os.getenv("OPENAI_MODEL", "gpt-4"),
    "api_key": os.getenv("OPENAI_API_KEY"),
    "temperature": float(os.getenv("OPENAI_TEMPERATURE", 0.7)),
    "max_tokens": int(os.getenv("OPENAI_MAX_TOKENS", 2000)),
    "timeout": int(os.getenv("AGENT_TIMEOUT", 300)),
}

# Agent Configuration
agent_config = {
    "timeout": int(os.getenv("AGENT_TIMEOUT", 300)),
    "max_iterations": int(os.getenv("MAX_ITERATIONS", 10)),
    "verbose": os.getenv("VERBOSE", "True").lower() == "true",
}

# AutoGen Configuration
autogen_config = {
    "seed": 42,
    "temperature": float(os.getenv("OPENAI_TEMPERATURE", 0.7)),
}
