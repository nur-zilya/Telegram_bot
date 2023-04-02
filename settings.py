import os

from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr, StrictStr

load_dotenv()

class SiteSettings(BaseSettings):
    api_key: SecretStr = os.getenv("SITE_API", None)
    host_api: StrictStr =  os.getenv("HOST_API", None)
