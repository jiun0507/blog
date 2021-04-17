from django.urls import path

from financial_statement.views import FinancialStatementView

urlpatterns = [
    path("", FinancialStatementView.as_view(), name="financial_statement"),
]