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
        typ = request.GET.get("type", "Y")
        limit = int(request.GET.get("limit", 1))
        page = int(request.GET.get("page", 1))

        polygon_financila_statements = polygon.get_polygon_financial_statement(
            ticker,
            limit=limit,
            typ=typ,
        )

        financial_statements = polygon_financila_statements[page - 1 : 1]

        context = {
            "stock": ticker,
            "financial_statements": financial_statements,
        }

        return render(request, "get_financial_statement.html", context=context)