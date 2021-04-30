from django.shortcuts import render

from company.models import CompanyModel
from financial_statement.models import FinancialStatement
from notification.models import Notification
from user.models import User
from valuation.models import Valuation
from company.use_case.get_company_profile import CompanyProfileUseCase


def home_view(request):
    financial_statements = FinancialStatement.objects.all().order_by("-id")[:10]
    notifications = Notification.objects.all().order_by("-id")[:10]
    valuations = Valuation.objects.all().order_by("-id")[:10]
    companies = CompanyModel.objects.all().order_by("-id")[:10]
    context = {
        "financial_statements": financial_statements,
        "notifications": notifications,
        "valuations": valuations,
        "companies": companies,
    }

    return render(request, "home.html", context=context)


def search(request):

    company_profile_use_case = CompanyProfileUseCase()

    input = request.GET.get("input")

    ticker_search_list = company_profile_use_case.get_company_profile_list_by_ticker(
        ticker=input
    )
    name_search_list = company_profile_use_case.get_company_profile_list_by_name(
        name=input
    )

    context = {
        "ticker_list": ticker_search_list,
        "name_list": name_search_list,
    }
    return render(request, template_name="search.html", context=context)
