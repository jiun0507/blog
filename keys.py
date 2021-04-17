from dotenv import load_dotenv
import os


class Keys:
    def __init__(self):
        load_dotenv()  # take environment variables from .env.
        self.polygon_api_key = os.getenv("polygon_api_key")
