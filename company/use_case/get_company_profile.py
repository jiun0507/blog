from django.http.response import Http404

from company.models import CompanyModel


class CompanyProfileUseCase:
    def get_company_profile(self, id):
        try:
            company = CompanyModel.objects.get(id=id)
        except CompanyModel.DoesNotExist:
            raise Http404

        return company

    def get_company_profile_list_by_name(self, name):
        try:
            companies = CompanyModel.objects.filter(name=name)
        except CompanyModel.DoesNotExist:
            raise Http404

        return companies

    def get_company_profile_list_by_ticker(self, ticker):
        try:
            companies = CompanyModel.objects.filter(ticker=ticker)
        except CompanyModel.DoesNotExist:
            raise Http404

        return companies