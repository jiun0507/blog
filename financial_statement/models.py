from django.db import models


class FinancialStatement(models.Model):
    data_source = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    period = models.CharField(max_length=10)
    calendar_date = models.DateTimeField(max_length=20)
    report_period = models.DateTimeField(max_length=20)
    updated = models.DateTimeField(max_length=20)
    enterprise_value = models.IntegerField()
    enterprise_value_over_EBIT = models.IntegerField()
    enterprise_value_over_EBITDA = models.IntegerField()
    payout_ratio = models.IntegerField()
    price_to_book_value = models.IntegerField()
    price_earnings = models.IntegerField()
    price_to_earnings = models.IntegerField()
    price_to_earnings_ratio = models.IntegerField()
    preferred_dividends_income_statement_impact = models.IntegerField()
    share_price_adjusted_close = models.IntegerField()
    price_sales = models.IntegerField()
    price_to_sales_ratio = models.IntegerField()
    return_on_average_assets = models.IntegerField()
    return_on_average_equity = models.IntegerField()
    return_on_invested_capital = models.IntegerField()
    return_on_sales = models.IntegerField()
    shares = models.IntegerField()
    weighted_average_shares = models.IntegerField()
    weighted_average_shares_diluted = models.IntegerField()
    sales_per_share = models.IntegerField()
    tangible_assets_book_value_per_share = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["symbol", "period", "calendar_date", "report_period"],
                name="financial statement quarterly/yearly restraint",
            )
        ]
