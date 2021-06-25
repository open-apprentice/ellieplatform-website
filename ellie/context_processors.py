import sys
from django.urls import resolve


def global_vars(request):
    return {
        'GLOBAL_TWITTER_ACCOUNT': '@open_apprentice',
        'ORGANIZATION_NAME': 'Open Apprentice Foundation',
        'ORGANIZATION_WEBSITE': 'https://openapprentice.org',
        'ORGANIZATION_LOGO': '/static/img/ellie/open-apprentice-logo-full.png',  # relative URL with pre /,
        'SITE_LOGO_URL': '/static/img/ellie/ellie-platform-logo.png',  # relative URL with pre /
        'APPNAME': sys.modules[resolve(request.path_info).func.__module__].__package__,
    }
