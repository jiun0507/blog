from django.urls import path

from financial_statement.views import FinancialStatementListView, FinancialStatementView

# This must be same as the namespace in the config.urls.py
# This allows this view to be used as a url tag in the html.
app_name = "financial_statement"

urlpatterns = [
    path("", FinancialStatementListView.as_view(), name="financial_statement_list"),
    path("<int:id>/", FinancialStatementView.as_view(), name="financial_statement"),
]