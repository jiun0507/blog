from Interface.iex_api import IEXInterface
from django.core.management.base import BaseCommand, CommandError
from company.models import CompanyModel
from Interface.polygon_api import PolygonInterface
from keys import Keys


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        # parser.add_argument("start", type=int)
        pass

    def handle(self, *args, **options):
        iex_interface = IEXInterface(Keys())
        companies = CompanyModel.objects.filter(notification__isnull=False)
        for company in companies:
            price = iex_interface.get_ticker_quote(ticker=company.ticker)
