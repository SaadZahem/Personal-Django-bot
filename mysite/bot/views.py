from django.shortcuts import render
from pprint import pformat

# Create your views here.

def update(request):
    return render(request, 'bot/view.html', dict(update=pformat(request.__dict__)))
