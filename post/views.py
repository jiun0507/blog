from django.views import View
from post.models import Log, Post
from django.shortcuts import redirect, render


class PostView(View):
    def get(self, request):
        try:
            posts = Post.objects.filter()
        except Post.DoesNotExist:
            return redirect("404.html")
        context = {
            "posts": posts,
        }
        return render(request, "post/posts.html", context=context)


class LogView(View):
    def get(self, request):
        logs = Log.objects.filter()
        context = {
            "logs": logs,
        }
        return render(request, "log/logs.html", context=context)
