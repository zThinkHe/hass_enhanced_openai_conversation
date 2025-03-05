"""Constants for the OpenAI Conversation integration."""

import logging

DOMAIN = "openai_conversation"
LOGGER = logging.getLogger(__package__)

CONF_SERVICE_NAME = "service name"
CONF_BASE_URL = "base_url"
CONF_RECOMMENDED = "recommended"
CONF_PROMPT = "prompt"
CONF_CHAT_MODEL = "chat_model"
RECOMMENDED_CHAT_MODEL = "doubao-1-5-pro-32k-250115"
CONF_MAX_TOKENS = "max_tokens"
RECOMMENDED_MAX_TOKENS = 150
CONF_TOP_P = "top_p"
RECOMMENDED_TOP_P = 1.0
CONF_TEMPERATURE = "temperature"
RECOMMENDED_TEMPERATURE = 1.0
