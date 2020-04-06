from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
from .forms import JsonForm
from .models import EntryForm
import json

# Create your views here.


def home(request):
    form = JsonForm()
    data = EntryForm.objects.all()

    if request.method == 'POST':
        form = JsonForm(request.POST)
        if form.is_valid():
            form.save()

            blog = EntryForm.objects.values().latest('id')
            json_object = json.dumps(blog, cls=DjangoJSONEncoder)
            with open("sample.json", "w") as outfile:
                outfile.write(json_object)
            return redirect('/')

    context = {'form': form, 'data': data}
    return render(request, 'form/home.html', context)
