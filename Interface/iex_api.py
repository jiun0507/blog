import requests
import json

import requests


class IEXInterface:
    def __init__(self, key):
        self.host = key.iex_host
        self.iex_key = key.iex_secret_key

    def get_ticker_quote(self, ticker):
        # print("\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++")
        path = "stable/stock/{0}/quote/latestPrice".format(ticker)
        url = self.host + path
        r = requests.get(
            url,
            params={"token": self.iex_key},
        )

        # print("\nRESPONSE++++++++++++++++++++++++++++++++++++")
        # print("Response code: %d\n" % r.status_code)

        return r.text

    def get_chart_data(self, ticker, range):
        # /stock/{symbol}/chart/{range}/{date}
        # print("\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++")
        path = "stable/stock/{0}/chart/{1}".format(ticker, range)
        url = self.host + path
        print(url)
        r = requests.get(
            url,
            params={"token": self.iex_key},
        )

        # print("\nRESPONSE++++++++++++++++++++++++++++++++++++")
        # print("Response code: %d\n" % r.status_code)
        return r.json()