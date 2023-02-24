import logging
import sys

from pydantic import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    index: str = Field(default="bets")
    amt_bets_to_generate: int = Field(default=2000)
    opensearch_url: str = Field(default="http://localhost:9200/")


root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

logger = root
settings = Settings()
