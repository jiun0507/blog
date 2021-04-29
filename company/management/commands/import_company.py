from django.core.management.base import BaseCommand, CommandError
from polygon.rest.models.definitions import Company
from company.models import CompanyModel
from Interface.polygon_api import PolygonInterface
from keys import Keys


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("start", type=int)
        parser.add_argument("end", type=int)

    def handle(self, *args, **options):
        start = options["start"]
        end = options["end"]
        self.polygon = PolygonInterface(Keys())
        for page_num in list(range(start, end)):
            tickers = self.polygon.get_polygon_company_list(page=page_num)
            for ticker in tickers:
                company = CompanyModel(
                    ticker=ticker["ticker"],
                    name=ticker["name"],
                    market=ticker["market"],
                    locale=ticker["locale"],
                    active=ticker["active"],
                )
                company.save()
