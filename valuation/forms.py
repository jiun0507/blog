from django import forms
from . import models


class ValuationForm(forms.Form):
    DCF = "dcf"
    REPRODUCTIOIN_COST = "reproduction_cst"
    OTHER = "other"
    METHOD_CHOICES = (
        (DCF, "DCF"),
        (REPRODUCTIOIN_COST, "Reproduction_cost"),
        (OTHER, "Other"),
    )

    review = forms.CharField()
    ticker = forms.CharField()
    method = forms.ChoiceField(choices=METHOD_CHOICES)
    value = forms.FloatField()
    formula = forms.CharField()
    financial_statement_id = forms.IntegerField(widget=forms.HiddenInput())

    # financial_statement_id.widget.attrs.update({"readonly": True})
    financial_statement_id.widget.attrs["readonly"] = True

    def clean(self):
        review = self.cleaned_data.get("review")
        ticker = self.cleaned_data.get("ticker")
        method = self.cleaned_data.get("method")
        value = self.cleaned_data.get("value")
        formula = self.cleaned_data.get("formula")

        if "process" in self.data:
            raise forms.ValidationError("The formula is computed.")
        else:
            raise forms.ValidationError("This is submit")

        if ticker == None or value == None or method == None:
            return None

        return self.cleaned_data