from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View

from post.models import Log, Post


def list_post(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        return redirect("404.html")
    context = {
        "posts": posts,
    }
    return render(request, "post/posts.html", context=context)


class PostView(View):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise Http404
        context = {
            "post": post,
        }
        return render(request, "post/post.html", context=context)


class LogView(View):
    def get(self, request):
        logs = Log.objects.all()
        context = {
            "logs": logs,
        }
        return render(request, "log/logs.html", context=context)
