from dotenv import load_dotenv
import os


class Keys:
    def __init__(self):
        load_dotenv()  # take environment variables from .env.
        self.alpaca_api_id = os.getenv("alpaca_api_id")
        self.alpaca_key = os.getenv("alpaca_key")
        print(self.alpaca_api_id)
        print(self.alpaca_key)
