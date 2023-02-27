from opensearchpy import OpenSearch

from src import config
from src import generators


settings = config.settings
logger = config.logger


def retrieve_sql(client, index: str):
    response = client.transport.perform_request(
        method='POST',
        url='/_plugins/_sql',
        params={"format": "json"},
        body={'query': f"SELECT * FROM {index} WHERE client.application_version = 'v2' LIMIT 5"},
    )
    return response


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
    results = retrieve_sql(os_client, index=settings.index)
    logger.info(results)
