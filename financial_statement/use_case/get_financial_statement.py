from Interface.polygon_api import PolygonInterface
from keys import Keys
from financial_statement.models import FinancialStatement


class GetFinancialStatementUseCase:
    def __init__(self):
        self.polygon = PolygonInterface(Keys())

    def get_financial_statement(self, ticker, page_size, page, period):
        try:
            limit = page_size * page
            offset = limit - page_size
            financial_statements = FinancialStatement.objects.filter(
                ticker=ticker, period=period
            )[offset:limit]
            if len(financial_statements) < limit:
                polygon_financial_statements = (
                    self.polygon.get_polygon_financial_statement(
                        ticker,
                        limit=limit,
                        type_=period,
                    )
                )

                # print(polygon_financial_statements)
                polygon_financial_statements = self.polygon.map_polygon_fs_to_fs_entity(
                    polygon_financial_statements
                )

                if len(financial_statements) < len(polygon_financial_statements):
                    financial_statements = polygon_financial_statements
                    for polygon_fs in polygon_financial_statements:
                        polygon_fs.save()

        except Exception as err:
            print(err)
            return []

        return financial_statements