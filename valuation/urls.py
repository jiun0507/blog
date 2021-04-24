from django.urls import path

from valuation.views import ValuationPage, ValuationTestView, ValuationView

app_name = "valuation"

urlpatterns = [
    path("", ValuationPage, name="valuation_page"),
    path("report/", ValuationTestView.as_view(), name="report"),
]