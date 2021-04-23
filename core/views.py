from django.shortcuts import render
from financial_statement.models import FinancialStatement


def home_view(request):
    financial_statements = FinancialStatement.objects.all().order_by("-id")[:10]
    options = ["financial statement", "valuation", "user"]
    context = {
        "financial_statements": financial_statements,
        "options": options,
    }

    return render(request, "home.html", context=context)


def search(request):
    input = request.GET.get("input")
    options = ["financial statement", "valuation", "user"]
    context = {
        "input": input,
        "options": options,
    }
    return render(request, template_name="search.html", context=context)
