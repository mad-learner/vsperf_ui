from django.forms import ModelForm
from .models import EntryForm


class JsonForm(ModelForm):
    class Meta:
        model = EntryForm
        fields = '__all__'
