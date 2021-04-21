from dataclasses import dataclass
from datetime import datetime

from django.db import models
from django.db.models.fields import DateTimeField
from django.urls import reverse


@dataclass
class FinancialStatementEntity:
    ticker: str
    period: str
    calendar_date: str
    report_period: str
    updated: str
    accumulated_other_comprehensive_income: int
    assets: int
    assets_average: int
    assets_current: int
    asset_turnover: int
    assets_non_current: int
    book_value_per_share: int
    capital_expenditure: int
    cash_and_equivalents: int
    cash_and_equivalentsUSD: int
    cost_of_revenue: int
    consolidated_income: int
    current_ratio: int
    debt_to_equity_ratio: int
    debt: int
    debt_current: int
    debt_non_current: int
    debtUSD: int
    deferred_revenue: int
    depreciation_amortization_and_accretion: int
    deposits: int
    dividend_yield: int
    dividends_per_basic_common_share: int
    earning_before_interest_taxes: int
    earnings_before_interest_taxes_depreciation_amortization: int
    EBITDA_margin: int
    earnings_before_interest_taxes_depreciation_amortizationUSD: int
    earning_before_interest_taxesUSD: int
    earnings_before_tax: int
    earnings_per_basic_share: int
    earnings_per_diluted_share: int
    earnings_per_basic_shareUSD: int
    shareholders_equity: int
    average_equity: int
    shareholders_equityUSD: int
    enterprise_value: int
    enterprise_value_overEBIT: int
    enterprise_value_overEBITDA: int
    free_cash_flow: int
    free_cash_flow_per_share: int
    foreign_currencyUSD_exchange_Rate: int
    gross_profit: int
    gross_margin: int
    goodwill_and_intangible_assets: int
    interest_expense: int
    invested_Capital: int
    invested_capital_average: int
    inventory: int
    investments: int
    investments_Current: int
    investments_non_current: int
    total_liabilities: int
    current_liabilities: int
    liabilities_non_current: int
    market_capitalization: int
    net_cash_flow: int
    net_cash_flow_business_acquisitions_disposals: int
    issuance_equity_shares: int
    issuance_debt_securities: int
    payment_dividends_other_cash_distributions: int
    net_cash_flow_from_financing: int
    net_cash_flow_from_investing: int
    net_cash_flow_investment_acquisitions_disposals: int
    net_cash_flow_from_operations: int
    effect_of_exchange_rate_changes_on_cash: int
    net_income: int
    net_income_common_stock: int
    net_income_common_stockUSD: int
    net_loss_income_from_discontinued_operations: int
    net_income_to_non_controlling_interests: int
    profit_margin: int
    operating_expenses: int
    operating_income: int
    trade_and_non_trade_payables: int
    payout_ratio: int
    price_to_book_value: int
    price_earnings: int
    price_to_earnings_ratio: int
    property_plant_equipment_net: int
    preferred_dividends_income_statement_impact: int
    share_price_adjusted_close: int
    price_sales: int
    price_to_sales_ratio: int
    trade_and_non_trade_receivables: int
    accumulated_retained_earnings_deficit: int
    revenues: int
    revenuesUSD: int
    research_and_development_expense: int
    return_on_average_assets: int
    return_on_average_equity: int
    return_on_invested_capital: int
    return_on_sales: int
    share_based_compensation: int
    selling_general_and_administrative_expense: int
    share_factor: int
    shares: int
    weighted_average_shares: int
    weighted_average_shares_diluted: int
    sales_per_share: int
    tangible_asset_value: int
    tax_assets: int
    income_tax_expense: int
    tax_liabilities: int
    tangible_assets_book_value_per_share: int
    working_capital: int


class FinancialStatement(models.Model):
    ticker = models.CharField(max_length=10)
    period = models.CharField(max_length=10)
    calendar_date = models.CharField(max_length=10)
    report_period = models.CharField(max_length=10)
    updated = models.CharField(max_length=10)
    accumulated_other_comprehensive_income = models.IntegerField()
    assets = models.IntegerField()
    assets_average = models.IntegerField()
    assets_current = models.IntegerField()
    asset_turnover = models.IntegerField()
    assets_non_current = models.IntegerField()
    book_value_per_share = models.IntegerField()
    capital_expenditure = models.IntegerField()
    cash_and_equivalents = models.IntegerField()
    cash_and_equivalentsUSD = models.IntegerField()
    cost_of_revenue = models.IntegerField()
    consolidated_income = models.IntegerField()
    current_ratio = models.IntegerField()
    debt_to_equity_ratio = models.IntegerField()
    debt = models.IntegerField()
    debt_current = models.IntegerField()
    debt_non_current = models.IntegerField()
    debtUSD = models.IntegerField()
    deferred_revenue = models.IntegerField()
    depreciation_amortization_and_accretion = models.IntegerField()
    deposits = models.IntegerField()
    dividend_yield = models.IntegerField()
    dividends_per_basic_common_share = models.IntegerField()
    earning_before_interest_taxes = models.IntegerField()
    earnings_before_interest_taxes_depreciation_amortization = models.IntegerField()
    EBITDA_margin = models.IntegerField()
    earnings_before_interest_taxes_depreciation_amortizationUSD = models.IntegerField()
    earning_before_interest_taxesUSD = models.IntegerField()
    earnings_before_tax = models.IntegerField()
    earnings_per_basic_share = models.IntegerField()
    earnings_per_diluted_share = models.IntegerField()
    earnings_per_basic_shareUSD = models.IntegerField()
    shareholders_equity = models.IntegerField()
    average_equity = models.IntegerField()
    shareholders_equityUSD = models.IntegerField()
    enterprise_value = models.IntegerField()
    enterprise_value_overEBIT = models.IntegerField()
    enterprise_value_overEBITDA = models.IntegerField()
    free_cash_flow = models.IntegerField()
    free_cash_flow_per_share = models.IntegerField()
    foreign_currencyUSD_exchange_Rate = models.IntegerField()
    gross_profit = models.IntegerField()
    gross_margin = models.IntegerField()
    goodwill_and_intangible_assets = models.IntegerField()
    interest_expense = models.IntegerField()
    invested_Capital = models.IntegerField()
    invested_capital_average = models.IntegerField()
    inventory = models.IntegerField()
    investments = models.IntegerField()
    investments_Current = models.IntegerField()
    investments_non_current = models.IntegerField()
    total_liabilities = models.IntegerField()
    current_liabilities = models.IntegerField()
    liabilities_non_current = models.IntegerField()
    market_capitalization = models.IntegerField()
    net_cash_flow = models.IntegerField()
    net_cash_flow_business_acquisitions_disposals = models.IntegerField()
    issuance_equity_shares = models.IntegerField()
    issuance_debt_securities = models.IntegerField()
    payment_dividends_other_cash_distributions = models.IntegerField()
    net_cash_flow_from_financing = models.IntegerField()
    net_cash_flow_from_investing = models.IntegerField()
    net_cash_flow_investment_acquisitions_disposals = models.IntegerField()
    net_cash_flow_from_operations = models.IntegerField()
    effect_of_exchange_rate_changes_on_cash = models.IntegerField()
    net_income = models.IntegerField()
    net_income_common_stock = models.IntegerField()
    net_income_common_stockUSD = models.IntegerField()
    net_loss_income_from_discontinued_operations = models.IntegerField()
    net_income_to_non_controlling_interests = models.IntegerField()
    profit_margin = models.IntegerField()
    operating_expenses = models.IntegerField()
    operating_income = models.IntegerField()
    trade_and_non_trade_payables = models.IntegerField()
    payout_ratio = models.IntegerField()
    price_to_book_value = models.IntegerField()
    price_earnings = models.IntegerField()
    price_to_earnings_ratio = models.IntegerField()
    property_plant_equipment_net = models.IntegerField()
    preferred_dividends_income_statement_impact = models.IntegerField()
    share_price_adjusted_close = models.IntegerField()
    price_sales = models.IntegerField()
    price_to_sales_ratio = models.IntegerField()
    trade_and_non_trade_receivables = models.IntegerField()
    accumulated_retained_earnings_deficit = models.IntegerField()
    revenues = models.IntegerField()
    revenuesUSD = models.IntegerField()
    research_and_development_expense = models.IntegerField()
    return_on_average_assets = models.IntegerField()
    return_on_average_equity = models.IntegerField()
    return_on_invested_capital = models.IntegerField()
    return_on_sales = models.IntegerField()
    share_based_compensation = models.IntegerField()
    selling_general_and_administrative_expense = models.IntegerField()
    share_factor = models.IntegerField()
    shares = models.IntegerField()
    weighted_average_shares = models.IntegerField()
    weighted_average_shares_diluted = models.IntegerField()
    sales_per_share = models.IntegerField()
    tangible_asset_value = models.IntegerField()
    tax_assets = models.IntegerField()
    income_tax_expense = models.IntegerField()
    tax_liabilities = models.IntegerField()
    tangible_assets_book_value_per_share = models.IntegerField()
    working_capital = models.IntegerField()

    def get_absolute_url(self):
        return reverse(
            "financial_statement:financial_statement", kwargs={"id": self.id}
        )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["ticker", "period", "calendar_date", "report_period"],
                name="financial statement quarterly/yearly restraint",
            ),
        ]
