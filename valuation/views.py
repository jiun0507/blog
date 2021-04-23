from django.http import HttpResponse
from django.shortcuts import render
from Interface.polygon_api import PolygonInterface
from django.views import View
from keys import Keys


def ValuationPage(request):
    return render(request, "markdown_template.html")


class ValuationView(View):
    def post(self, request):

        return HttpResponse("This is financial statements app.")