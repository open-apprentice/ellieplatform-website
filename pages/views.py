from django.shortcuts import render, get_object_or_404
from .models import Page


def single_page(request, slug):
    page = get_object_or_404(Page, slug=slug, status='published')

    context = {
        'page': page
    }

    return render(request, 'pages/single_page.html', context)

