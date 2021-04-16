from os import get_blocking

from django.http import HttpResponse
from django.shortcuts import render
from Interface.alpaca_interface import PolygonInterface
from keys import Keys

# Create your views here.
def get(request):
    key = Keys()
    polygon = PolygonInterface(key)
    ticker = request.GET.get("ticker", "AAPL")

    polygon_financila_statements = polygon.get_polygon_financial_statement(ticker)
    print(polygon_financila_statements)

    return HttpResponse("This is financial statements app.")