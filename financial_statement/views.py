import json
from math import ceil

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from financial_statement.use_case.get_financial_statement import (
    FinancialStatementUseCase,
)
from django.http import Http404


class FinancialStatementView(View):
    def __init__(self):
        self.use_case = FinancialStatementUseCase()

    def get(self, request, id):
        try:
            financial_statement = self.use_case.get_financial_statement(id)
        except Exception as err:
            raise Http404()

        context = {
            "financial_statement": financial_statement,
        }

        return render(request, "get_financial_statement.html", context=context)


class FinancialStatementListView(View):
    def __init__(self):
        self.use_case = FinancialStatementUseCase()

    def get(self, request):
        page_size = 5
        ticker = request.GET.get("ticker", "AAPL") or "AAPL"
        period = request.GET.get("period", "Y") or "Y"
        page = int(request.GET.get("page", 1)) or 1

        financial_statements = self.use_case.get_financial_statement_list(
            ticker=ticker, page_size=page_size, page=page, period=period
        )

        page_limit = ceil(len(financial_statements) / page_size)

        if page_limit == 0:
            return redirect("http_404.html")

        print(ticker, financial_statements, page, page_limit)
        context = {
            "stock": ticker,
            "financial_statements": financial_statements,
            "page": page,
            "page_limit": page_limit,
        }

        return render(request, "get_financial_statement_list.html", context=context)

    def post(self, request):
        body = json.loads(request.body)
        ticker = body.get("ticker", "AAPL") or "AAPL"
        period = body.get("period", "Y") or "Y"
        limit = body.get("limit", 1) or 1

        self.use_case.post_financial_statement(
            ticker=ticker, limit=limit, period=period
        )

        return HttpResponse("Successfully posted")