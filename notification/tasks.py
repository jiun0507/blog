from Interface.polygon_api import PolygonInterface
from Interface.iex_api import IEXInterface
from company.models import CompanyModel
from notification.models import Notification
from keys import Keys
from django.utils import timezone


def stock_price_notification():
    result = ""
    try:
        now = timezone.now()
        iex_interface = IEXInterface(Keys())
        polygon = PolygonInterface(Keys())
        market_status = polygon.get_market_status_now()

        if market_status.exchanges["nyse"] == "closed":
            print("It's " + now + "Market closed....")
            return "It's " + now + "Market closed...."
        companies = CompanyModel.objects.filter(notification__isnull=False)
        result = (
            now + ": There are " + len(companies) + " of companies to keep track of.\n"
        )

        for company in companies:
            price = iex_interface.get_ticker_quote(ticker=company.ticker)
            notifications = Notification.objects.filter(
                price__gte=price, company=company
            )
            result += (
                company.name
                + " : "
                + len(notifications)
                + " number of notifications sent."
            )
            for notification in notifications:
                pass
    except:
        pass
    return result