import datetime
import typing as tp

from faker import Faker
import numpy as np


class BetGenerator:

    def __init__(self):
        self.faker = Faker()

    def __generate_credit_card(self) -> dict[str, tp.Union[str, int, float]]:
        return {
            "expire_date": self.faker.credit_card_expire(),
            "number": self.faker.credit_card_number(),
            "provider": self.faker.credit_card_provider(),
            "security_code": self.faker.credit_card_security_code(),
        }

    def __generate_money_details(self) -> dict[str, tp.Union[str, int, float]]:
        money_amt = self.faker.random.normalvariate(mu=100, sigma=40)
        money_amt = round(np.clip(money_amt, a_min=1, a_max=money_amt), 4)
        currency = self.faker.currency()
        return {
            "currency_code": currency[0],
            "currency_name": currency[1],
            "amount": money_amt,
        }

    def __generate_person(self) -> dict[str, tp.Union[str, int, float]]:
        return {
            "first_name": self.faker.first_name_male(),
            "last_name": self.faker.last_name_male(),
        }

    def __generate_client_details(self):
        if self.faker.boolean(60):
            platform_token = self.faker.android_platform_token
        else:
            platform_token = self.faker.ios_platform_token
        return {
            "device": platform_token(),
            "application_version": self.faker.random.choice(["v2", "v3", "v4"]),
        }

    def __generate_event_timestamp(self) -> str:
        return str(datetime.datetime.now())

    def generate(self) -> dict:
        return {
            "transaction": {
                "money": self.__generate_money_details(),
                "credit_card": self.__generate_credit_card(),
            },
            "user": self.__generate_person(),
            "client": self.__generate_client_details(),
            "event": {
                "id": self.faker.uuid4(),
                "timestamp": self.__generate_event_timestamp(),
            },
        }
