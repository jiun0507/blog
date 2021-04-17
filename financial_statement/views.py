from os import get_blocking

from django.http import HttpResponse
from django.shortcuts import render
from Interface.polygon_api import PolygonInterface

# Create your views here.
def get(request):
    polygon = PolygonInterface()
    ticker = request.GET.get("ticker", "AAPL")

    polygon_financila_statements = polygon.get_polygon_financial_statement(ticker)
    print(len(polygon_financila_statements))
    print(polygon_financila_statements[0])

    return HttpResponse("This is financial statements app.")