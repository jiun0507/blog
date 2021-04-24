import json
from email.quoprimime import body_decode

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views import View
from django.views.generic.edit import FormView

from Interface.polygon_api import PolygonInterface
from keys import Keys

from . import forms


def ValuationPage(request):
    return render(request, "markdown_template.html")


class ValuationView(FormView):
    template_name = "valuation_template.html"
    form_class = forms.ValuationForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        ticker = form.cleaned_data.get("ticker")
        return super().form_valid(form)


class ValuationTestView(View):
    def get(self, request):
        id = 15
        initial = {
            "financial_statement_id": id,
        }
        form = forms.ValuationForm(initial=initial)
        financial_statement = {}
        return render(
            request,
            "valuation_template.html",
            context={"form": form, "financial_statement": financial_statement},
        )

    def post(self, request):
        form = forms.ValuationForm(request.POST)
        if form.is_valid():
            return redirect(
                reverse("core:home")
            )  # Should be reirected to a success page.
        myDict = dict(request.POST.lists())
        if "process" in myDict:
            print("This is a process")
        if "submit" in myDict:
            print("this is submit")
        return render(request, "valuation_template.html", context={"form": form})