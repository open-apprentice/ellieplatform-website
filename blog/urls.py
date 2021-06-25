from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.blog_post, name='blog_post'),
    path('category/<slug:slug>/', views.category_post_list, name='category'),
    path('author/<str:author>', views.author_post_list, name='author'),
]
