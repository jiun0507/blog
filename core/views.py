from django.shortcuts import render

from notification.models import Notification
from valuation.models import Valuation
from post.models import Post


def home_view(request):
    posts = Post.objects.all().order_by("-id")[:4]
    for post in posts:
        post.content = post.content[:100]
    notifications = Notification.objects.all().order_by("-id")[:10]
    valuations = Valuation.objects.all().order_by("-id")[:10]
    context = {
        "notifications": notifications,
        "valuations": valuations,
        "posts": posts,
    }

    return render(request, "home.html", context=context)
