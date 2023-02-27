from opensearchpy import OpenSearch

import pandas as pd

from src import config
from src import generators


settings = config.settings
logger = config.logger


def factory_bulk_index_action(
        bets: list[dict],
        index: str,
) -> list[str, dict]:
    actions = []
    for _id, bet in enumerate(bets):
        action = {"index": {"_index": index}}
        actions.append(action)
        actions.append(bet)
    return actions


if __name__ == "__main__":

    os_client = OpenSearch(
        hosts=settings.opensearch_hosts,
        http_compress=True,
        use_ssl=True,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )

    logger.info(os_client.info())
    bets = generators.generate_fake_bets(settings.amt_bets_to_generate)
    bets = pd.json_normalize(bets).to_dict("records")
    bulk_index_body = factory_bulk_index_action(bets, index=settings.index)
    response = os_client.bulk(body=bulk_index_body)
