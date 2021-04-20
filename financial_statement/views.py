from financial_statement.use_case.get_financial_statement import (
    FinancialStatementUseCase,
)
from math import ceil

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from Interface.polygon_api import PolygonInterface
from keys import Keys


class FinancialStatementView(View):
    def __init__(self):
        self.use_case = FinancialStatementUseCase()

    def get(self, request):
        page_size = 1
        ticker = request.GET.get("ticker", "AAPL") or "AAPL"
        period = request.GET.get("period", "Y") or "Y"
        page = int(request.GET.get("page", 1)) or 1

        financial_statements = self.use_case.get_financial_statement(
            ticker=ticker, page_size=page_size, page=page, period=period
        )

        page_limit = len(financial_statements)
        if page_limit == 0:
            return redirect("http_404.html")
        context = {
            "stock": ticker,
            "financial_statements": financial_statements,
            "page": page,
            "page_limit": page_limit,
        }

        return render(request, "get_financial_statement.html", context=context)