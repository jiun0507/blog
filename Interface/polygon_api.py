from polygon import RESTClient


"""
This is interface for polygon.io.
polygon-api-client library is used for REST requests.
python client github : https://github.com/polygon-io/client-python
available api can be referenced : https://github.com/polygon-io/client-python/blob/master/polygon/rest/client.py
return data types are here : https://github.com/polygon-io/client-python/blob/master/polygon/rest/models/definitions.py
"""


class PolygonInterface:
    def __init__(self, key):
        self.client = RESTClient(key.polygon_api_key)

    def get_polygon_financial_statement(self, symbol, limit=1):
        params = {}
        params["limit"] = limit
        financial_statement = self.client.reference_stock_financials(
            symbol=symbol,
            limit=limit,
        )
        return financial_statement.results
