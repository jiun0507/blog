from django.shortcuts import render

from company.models import CompanyModel
from financial_statement.models import FinancialStatement
from notification.models import Notification
from user.models import User
from valuation.models import Valuation
from company.use_case.get_company_profile import CompanyProfileUseCase
from post.models import Post


def home_view(request):
    posts = Post.objects.all().order_by("-id")[:4]
    notifications = Notification.objects.all().order_by("-id")[:10]
    valuations = Valuation.objects.all().order_by("-id")[:10]
    context = {
        "notifications": notifications,
        "valuations": valuations,
        "posts": posts,
    }

    return render(request, "home.html", context=context)
