from opensearchpy import OpenSearch

from src import config
from src import generators


settings = config.settings
logger = config.logger


def select_all(os_client):
    return os_client.search(
        index=settings.index,
        body={
            'query': {"match_all": {}},
        },
    )


def query_and_agg(os_client, index):
    return os_client.search(
        index=settings.index,
        body={
            'query': {"match": {"client.application_version": "v2"}},
            "aggs": {
                "total_device_count": {
                    "value_count": {"field": "client"},
                },
            },
        },
    )


if __name__ == "__main__":

    os_client = OpenSearch(
        hosts=settings.opensearch_hosts,
        http_compress=True,
        use_ssl=False,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )

    bets = generators.generate_fake_bets(1)
    response = query_and_agg(os_client, index=settings.index)
    logger.info(response["aggregations"])
