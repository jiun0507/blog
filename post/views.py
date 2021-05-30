from django.http.response import Http404
from django.shortcuts import render
from django.views import View
from post.models import Post


class PostView(View):
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return redirect("404.html")
        context = {
            "post": post,
        }
        return render(request, "post/post.html", context=context)
