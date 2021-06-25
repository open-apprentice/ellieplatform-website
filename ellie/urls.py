from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from django import contrib
from blog.sitemaps import PostSitemap
from pages.sitemaps import PageSitemap
from . import views

sitemaps = {
    'posts': PostSitemap,
    'single_pages': PageSitemap,
}

# https://overiq.com/django-1-10/handling-media-files-in-django/
regular_patterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('pages.urls', namespace='single_page')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml/', contrib.sitemaps.views.index, {'sitemaps': sitemaps}),
    path('sitemap-<str:section>.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

media_root = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static_root = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = regular_patterns + media_root + static_root
