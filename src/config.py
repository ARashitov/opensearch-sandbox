import logging
import sys

import pydantic


class Settings(pydantic.BaseSettings):
    index: str = pydantic.Field(default="bets")
    amt_bets_to_generate: int = pydantic.Field(default=5)
    opensearch_url: str = pydantic.Field(default="http://localhost:9200/")
    opensearch_hosts: list[pydantic.AnyHttpUrl] = pydantic.Field(
        default=[
            "http://localhost:9200/",
        ],
    )


root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

logger = root
settings = Settings()
