import os
import logging
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv

# Load .env from the nearest path (project root, parent dirs, etc.)
load_dotenv(find_dotenv(), override=False)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "na")
    openai_base_url: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    chat_model: str = os.getenv("CHAT_MODEL", "gpt-4o-mini")
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

settings = Settings()

if settings.openai_api_key in ("", "na"):
    logger.warning("OPENAI_API_KEY is not set (using default 'na'). Check your .env file.")

logger.info("Loaded settings: base_url=%s, chat_model=%s, embedding_model=%s",
            settings.openai_base_url, settings.chat_model, settings.embedding_model)
