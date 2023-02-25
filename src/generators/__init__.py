from .bet import BetGenerator


def generate_fake_bets(amt_bets: int) -> list[dict]:
    bet_generator = BetGenerator()
    bets = [
        bet_generator.generate()
        for bet_id in range(amt_bets)
    ]
    return bets
