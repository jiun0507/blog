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
