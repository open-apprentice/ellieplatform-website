from django.shortcuts import render, get_object_or_404
from .models import Post, Category, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts_list = Post.objects.filter(status="published")
    paginator = Paginator(posts_list, 5)  # change this to accommodate number of posts per page
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'page': page
    }

    return render(request, 'blog/post_list.html', context, )


def author_post_list(request, author):
    author = User.objects.get(username=author)

    posts_list = author.posts.filter(status="published")

    paginator = Paginator(posts_list, 3)  # change this to accommodate number of posts per page
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'author': author,
        'posts': posts,
        'page': page
    }

    return render(request, 'blog/author_post_list.html', context)


def category_post_list(request, slug):
    category = Category.objects.get(slug=slug)

    posts_list = category.posts.filter(status="published")
    paginator = Paginator(posts_list, 5)  # change this to accommodate number of posts per page

    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'posts': posts,
        'page': page
    }

    return render(request, 'blog/category.html', context)


def blog_post(request, slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug, status='published')

    context = {
        'post': post
    }

    return render(request, 'blog/blog_post.html', context)
