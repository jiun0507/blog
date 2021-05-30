"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# namespace is used to create url tags to be used in the html files
urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "financial_statement/",
        include("financial_statement.urls", namespace="financial_statement"),
    ),
    path("", include("core.urls", namespace="core")),
    path("valuation/", include("valuation.urls", namespace="valuation")),
    path("user/", include("user.urls", namespace="user")),
    path("company/", include("company.urls", namespace="company")),
    path("notification/", include("notification.urls", namespace="notification")),
    path("post/", include("post.urls", namespace="post")),
]
