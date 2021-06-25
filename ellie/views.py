from django.shortcuts import render
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'index.html', )


def index(request):
    return HttpResponseRedirect("/")
