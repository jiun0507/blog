from django.shortcuts import render
from financial_statement.models import FinancialStatement


def home_view(request):
    financial_statements = FinancialStatement.objects.all().order_by("-id")[:10]
    context = {
        "financial_statements": financial_statements,
    }

    return render(request, "home.html", context=context)