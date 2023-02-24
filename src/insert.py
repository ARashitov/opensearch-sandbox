import asyncio
import aiohttp
import requests

from src.config import logger
from src.config import settings
from src.decorators import timeit
from src.generators.bet import BetGenerator


@timeit
def sync_insert(bets: list[dict]) -> list[dict]:
    response = []
    with requests.Session() as session:
        for bet in bets:
            r = session.post(
                url=f"{settings.opensearch_url}{settings.index}/_doc",
                json=bet,
            )
            response.append(r.json())
    return response


async def ingest(url, bet, session):
    async with session.post(url, json=bet) as response:
        return await response.json()


@timeit
async def async_insert(bets: list[dict]):

    url = f"{settings.opensearch_url}{settings.index}/_doc"

    futures = []
    async with aiohttp.ClientSession() as session:

        for bet in bets:
            future = asyncio.ensure_future(ingest(url, bet, session))
            futures.append(future)

        responses = await asyncio.gather(*futures)

    return responses


if __name__ == "__main__":
    bet_generator = BetGenerator()
    bets = [
        bet_generator.generate()
        for bet_id in range(settings.amt_bets_to_generate)
    ]
    responses = sync_insert(bets)

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(async_insert(bets))
    responses = loop.run_until_complete(future)

    logger.info(responses[0])
