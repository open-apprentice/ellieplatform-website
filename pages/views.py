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
