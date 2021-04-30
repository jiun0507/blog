from notification.models import Notification


class NotificationUseCase:
    def add_notification(self, company, price, repeat, active, user):
        try:
            notification = Notification(
                company=company, price=price, repeat=repeat, active=active, user=user
            )
            notification.save()
        except Exception as err:
            raise err
        return notification