from django.contrib.sitemaps import Sitemap

from .models import Page


class PageSitemap(Sitemap):
    changefreq = 'daily'  # 'always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never'
    priority = 0.9

    def items(self):
        return Page.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated
