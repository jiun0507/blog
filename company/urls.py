from django.urls import path
from company.views import CompanyView

# This must be same as the namespace in the config.urls.py
# This allows this view to be used as a url tag in the html.
app_name = "company"

urlpatterns = [
    path("<int:id>/", CompanyView.as_view(), name="profile"),
]