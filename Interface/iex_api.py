import requests
import json


import sys, os, base64, datetime, hashlib, hmac
import requests  # pip install requests


class IEXInterface:
    def __init__(self, key):
        self.host = "https://cloud.iexapis.com/"
        self.iex_key = key.iex_secret_key

    def get_ticker_quote(self, ticker):
        print("\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++")
        path = "stable/stock/{0}/quote/latestPrice".format(ticker)
        url = self.host + path
        r = requests.get(
            url,
            params={"token": self.iex_key},
        )

        print("\nRESPONSE++++++++++++++++++++++++++++++++++++")
        print("Response code: %d\n" % r.status_code)
        print(r.text)

        return r.text