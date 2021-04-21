from Interface.polygon_api import PolygonInterface
from keys import Keys
from financial_statement.models import FinancialStatement


class FinancialStatementUseCase:
    def __init__(self):
        self.polygon = PolygonInterface(Keys())

    def get_financial_statement_list(self, ticker, page_size, page, period):
        try:
            limit = page_size * page
            offset = limit - page_size
            financial_statements = FinancialStatement.objects.filter(
                ticker=ticker, period=period
            )

        except Exception as err:
            print(err)
            return []

        return financial_statements[offset:limit]

    def get_financial_statement(self, id):
        try:
            financial_statement = FinancialStatement.objects.get(
                id=id,
            )
        except FinancialStatement.DoesNotExist as err:
            print(err)
            raise err
        return financial_statement

    def post_financial_statement(self, ticker, period, limit):
        try:
            polygon_financial_statements = self.polygon.get_polygon_financial_statement(
                ticker,
                limit=limit,
                type_=period,
            )
        except Exception as err:
            print(err)
            return []

        FinancialStatement.objects.bulk_create(polygon_financial_statements)
        return polygon_financial_statements