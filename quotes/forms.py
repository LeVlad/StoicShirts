from django import forms
from .models import StoicQuotes


class StoicQuotesForm(forms.ModelForm):

    class Meta:
        model = StoicQuotes
        fields = ["stoic", "most_popular"]