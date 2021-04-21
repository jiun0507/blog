from django.urls import path

from financial_statement.views import FinancialStatementListView, FinancialStatementView

app_name = "financial_statement"

urlpatterns = [
    path("", FinancialStatementListView.as_view(), name="financial_statement_list"),
    path("<int:id>/", FinancialStatementView.as_view(), name="financial_statement"),
]