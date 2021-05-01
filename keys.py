from dotenv import load_dotenv
import os


class Keys:
    def __init__(self):
        load_dotenv()  # take environment variables from .env.
        self.polygon_api_key = os.getenv(
            "polygon_api_key", "9RQWB5_yZSd_Bc2_x3Ox_b7MBoBC6An8tHBh6M"
        )
        self.iex_api_token = os.environ.get(
            "iex_api_token", "pk_a0d243db3a7341fb867c05737d3a2d03 "
        )
        self.iex_secret_key = os.environ.get(
            "iex_secret_key", "sk_520c3947d2c3426f94d81f6ecaf505c1"
        )
