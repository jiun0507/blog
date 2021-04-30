from company.use_case.get_company_profile import CompanyProfileUseCase
from django.shortcuts import render
from django.views import View


class CompanyView(View):
    def __init__(self):
        self.company_profile_use_case = CompanyProfileUseCase()

    def get(self, request, id):
        company = self.company_profile_use_case.get_company_profile(id=id)

        context = {
            "company": company,
        }
        return render(request, "company/company.html", context=context)