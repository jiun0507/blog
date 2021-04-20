from financial_statement.use_case.get_financial_statement import (
    FinancialStatementUseCase,
)
import json
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

    def post(self, request):
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        ticker = body.get("ticker", "AAPL")
        period = body.get("period", "Y") or "Y"
        limit = body.get("limit", 1) or 1

        self.use_case.post_financial_statement(
            ticker=ticker, limit=limit, period=period
        )

        return HttpResponse("Successfully posted")