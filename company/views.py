from company.use_case.get_company_profile import CompanyProfileUseCase
from django.shortcuts import render
from django.views import View
from Interface import iex_api
from keys import Keys
from django.utils.safestring import mark_safe
import json


class CompanyView(View):
    def __init__(self):
        self.company_profile_use_case = CompanyProfileUseCase()
        self.iex = iex_api.IEXInterface(Keys())

    def get(self, request, id):
        company = self.company_profile_use_case.get_company_profile(id=id)
        prices = self.iex.get_chart_data("aapl", "5d")
        context = {
            "company": company.__dict__,
            "prices": prices,
        }
        return render(request, "company/company.html", context=context)