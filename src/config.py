import logging
import sys

from opensearchpy import OpenSearch

import pydantic


class Settings(pydantic.BaseSettings):
    index: str = pydantic.Field(default="events_for_test")
    amt_bets_to_generate: int = pydantic.Field(default=10000)
    opensearch_url: str = pydantic.Field(default="https://localhost:9200/")
    opensearch_basic_auth: tuple[str, str] = pydantic.Field(default=("admin", "admin"))
    opensearch_hosts: list[pydantic.AnyHttpUrl] = ["https://admin:admin@localhost:9200/"]


root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

logger = root
settings = Settings()


client = OpenSearch(
    hosts=settings.opensearch_hosts,
    http_compress=True,
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)
