from django.shortcuts import render

# Create your views here.

def update(request):
    return render(request, 'bot/view.html', dict(update=request.__dict__))
