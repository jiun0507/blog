from os import get_blocking

from django.http import HttpResponse
from django.shortcuts import render
from Interface.polygon_api import PolygonInterface
from django.views import View
from keys import Keys
import json


class FinancialStatementView(View):
    def get(self, request):
        polygon = PolygonInterface(Keys())
        ticker = request.GET.get("ticker", "AAPL")

        polygon_financila_statements = polygon.get_polygon_financial_statement(
            ticker, limit=5
        )

        context = {
            "stock": ticker,
            "financial_statements": polygon_financila_statements,
        }
        return render(request, "get_financial_statement.html", context=context)