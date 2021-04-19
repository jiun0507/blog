from django.urls import path

from valuation.views import ValuationPage

urlpatterns = [
    path("", ValuationPage, name="valuation_page"),
]