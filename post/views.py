from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View
from django.core.paginator import Paginator
from post.models import Log, Post


def list_post(request):
    try:
        all_posts = Post.objects.all().order_by("-created_at")
        page = int(request.GET.get("p", 1))  # 없으면 1로 지정
        paginator = Paginator(all_posts, 5)  # 한 페이지 당 몇개 씩 보여줄 지 지정
        posts = paginator.get_page(page)
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
