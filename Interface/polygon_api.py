from polygon import RESTClient
from polygon.rest.models.definitions import Financial
from financial_statement.models import FinancialStatementEntity, FinancialStatement

"""
This is interface for polygon.io.
polygon-api-client library is used for REST requests.
python client github : https://github.com/polygon-io/client-python
available api can be referenced : https://github.com/polygon-io/client-python/blob/master/polygon/rest/client.py
return data types are here : https://github.com/polygon-io/client-python/blob/master/polygon/rest/models/definitions.py
"""


class PolygonInterface:
    def __init__(self, key):
        self.client = RESTClient(key.polygon_api_key)

    def map_polygon_fs_to_fs_entity(self, polygon_financial_statements):
        print(
            polygon_financial_statements[0]["calendarDate"],
            polygon_financial_statements[0]["reportPeriod"],
        )
        return [
            FinancialStatement(
                ticker=polygon_fs["ticker"],
                period=polygon_fs["period"],
                calendar_date=polygon_fs["calendarDate"],
                report_period=polygon_fs["reportPeriod"],
                updated=polygon_fs["updated"],
                accumulated_other_comprehensive_income=polygon_fs[
                    "accumulatedOtherComprehensiveIncome"
                ],
                assets=polygon_fs["assets"],
                assets_average=polygon_fs["assets"],
                assets_current=polygon_fs["assets"],
                asset_turnover=polygon_fs["assets"],
                assets_non_current=polygon_fs["assets"],
                book_value_per_share=polygon_fs["assets"],
                capital_expenditure=polygon_fs["assets"],
                cash_and_equivalents=polygon_fs["assets"],
                cash_and_equivalentsUSD=polygon_fs["assets"],
                cost_of_revenue=polygon_fs["assets"],
                consolidated_income=polygon_fs["assets"],
                current_ratio=polygon_fs["assets"],
                debt_to_equity_ratio=polygon_fs["assets"],
                debt=polygon_fs["assets"],
                debt_current=polygon_fs["assets"],
                debt_non_current=polygon_fs["assets"],
                debtUSD=polygon_fs["assets"],
                deferred_revenue=polygon_fs["assets"],
                depreciation_amortization_and_accretion=polygon_fs["assets"],
                deposits=polygon_fs["assets"],
                dividend_yield=polygon_fs["assets"],
                dividends_per_basic_common_share=polygon_fs["assets"],
                earning_before_interest_taxes=polygon_fs["assets"],
                earnings_before_interest_taxes_depreciation_amortization=polygon_fs[
                    "assets"
                ],
                EBITDA_margin=polygon_fs["assets"],
                earnings_before_interest_taxes_depreciation_amortizationUSD=polygon_fs[
                    "assets"
                ],
                earning_before_interest_taxesUSD=polygon_fs["assets"],
                earnings_before_tax=polygon_fs["assets"],
                earnings_per_basic_share=polygon_fs["assets"],
                earnings_per_diluted_share=polygon_fs["assets"],
                earnings_per_basic_shareUSD=polygon_fs["assets"],
                shareholders_equity=polygon_fs["assets"],
                average_equity=polygon_fs["assets"],
                shareholders_equityUSD=polygon_fs["assets"],
                enterprise_value=polygon_fs["assets"],
                enterprise_value_overEBIT=polygon_fs["assets"],
                enterprise_value_overEBITDA=polygon_fs["assets"],
                free_cash_flow=polygon_fs["assets"],
                free_cash_flow_per_share=polygon_fs["assets"],
                foreign_currencyUSD_exchange_Rate=polygon_fs["assets"],
                gross_profit=polygon_fs["assets"],
                gross_margin=polygon_fs["assets"],
                goodwill_and_intangible_assets=polygon_fs["assets"],
                interest_expense=polygon_fs["assets"],
                invested_Capital=polygon_fs["assets"],
                invested_capital_average=polygon_fs["assets"],
                inventory=polygon_fs["assets"],
                investments=polygon_fs["assets"],
                investments_Current=polygon_fs["assets"],
                investments_non_current=polygon_fs["assets"],
                total_liabilities=polygon_fs["assets"],
                current_liabilities=polygon_fs["assets"],
                liabilities_non_current=polygon_fs["assets"],
                market_capitalization=polygon_fs["assets"],
                net_cash_flow=polygon_fs["assets"],
                net_cash_flow_business_acquisitions_disposals=polygon_fs["assets"],
                issuance_equity_shares=polygon_fs["assets"],
                issuance_debt_securities=polygon_fs["assets"],
                payment_dividends_other_cash_distributions=polygon_fs["assets"],
                net_cash_flow_from_financing=polygon_fs["assets"],
                net_cash_flow_from_investing=polygon_fs["assets"],
                net_cash_flow_investment_acquisitions_disposals=polygon_fs["assets"],
                net_cash_flow_from_operations=polygon_fs["assets"],
                effect_of_exchange_rate_changes_on_cash=polygon_fs["assets"],
                net_income=polygon_fs["assets"],
                net_income_common_stock=polygon_fs["assets"],
                net_income_common_stockUSD=polygon_fs["assets"],
                net_loss_income_from_discontinued_operations=polygon_fs["assets"],
                net_income_to_non_controlling_interests=polygon_fs["assets"],
                profit_margin=polygon_fs["assets"],
                operating_expenses=polygon_fs["assets"],
                operating_income=polygon_fs["assets"],
                trade_and_non_trade_payables=polygon_fs["assets"],
                payout_ratio=polygon_fs["assets"],
                price_to_book_value=polygon_fs["assets"],
                price_earnings=polygon_fs["assets"],
                price_to_earnings_ratio=polygon_fs["assets"],
                property_plant_equipment_net=polygon_fs["assets"],
                preferred_dividends_income_statement_impact=polygon_fs["assets"],
                share_price_adjusted_close=polygon_fs["assets"],
                price_sales=polygon_fs["assets"],
                price_to_sales_ratio=polygon_fs["assets"],
                trade_and_non_trade_receivables=polygon_fs["assets"],
                accumulated_retained_earnings_deficit=polygon_fs["assets"],
                revenues=polygon_fs["assets"],
                revenuesUSD=polygon_fs["assets"],
                research_and_development_expense=polygon_fs["assets"],
                return_on_average_assets=polygon_fs["assets"],
                return_on_average_equity=polygon_fs["assets"],
                return_on_invested_capital=polygon_fs["assets"],
                return_on_sales=polygon_fs["assets"],
                share_based_compensation=polygon_fs["assets"],
                selling_general_and_administrative_expense=polygon_fs["assets"],
                share_factor=polygon_fs["assets"],
                shares=polygon_fs["assets"],
                weighted_average_shares=polygon_fs["assets"],
                weighted_average_shares_diluted=polygon_fs["assets"],
                sales_per_share=polygon_fs["assets"],
                tangible_asset_value=polygon_fs["assets"],
                tax_assets=polygon_fs["assets"],
                income_tax_expense=polygon_fs["assets"],
                tax_liabilities=polygon_fs["assets"],
                tangible_assets_book_value_per_share=polygon_fs["assets"],
                working_capital=polygon_fs["assets"],
            )
            for polygon_fs in polygon_financial_statements
        ]

    def get_polygon_financial_statement(self, symbol, limit=1, type_="Y"):
        financial_statement = self.client.reference_stock_financials(
            symbol=symbol,
            limit=limit,
            type=type_,
        )
        return financial_statement.results
