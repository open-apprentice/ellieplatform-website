from django.shortcuts import render, get_object_or_404
from .models import Page


def index(request):
    page = get_object_or_404(Page, slug='home', status='published')

    context = {
        'page': page
    }
    return render(request, 'pages/index.html', context)


def single_page(request, slug):
    page = get_object_or_404(Page, slug=slug, status='published')

    context = {
        'page': page
    }

    return render(request, 'pages/single_page.html', context)


def handler404(request, exception):
    return render(request, 'pages/not_found.html', status=404)


def handler500(request, *args, **argv):
    return render(request, 'pages/500.html', status=500)

