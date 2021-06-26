from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.single_page, name='single_page'),
]
