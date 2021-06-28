from django.shortcuts import render, get_object_or_404
from .models import Post, Category, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.db.models import Count
from django.utils import timezone


def post_list(request, tag_slug=None):
    posts = Post.objects.filter(status="published")
    latest_posts = Post.objects.filter(published_date__lte=timezone.now()).reverse()[:3]

    # post tag
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 5)  # change this to accommodate number of posts per page
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'page': page,
        'tag': tag,
        'latest_posts': latest_posts,
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
    paginator = Paginator(posts_list, 3)  # change this to accommodate number of posts per page

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

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(active=True, tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-active')[
                    :3]  # adjust slice here for amount of posts to show

    context = {
        'post': post,
        'similar_posts': similar_posts,
    }

    return render(request, 'blog/blog_post.html', context)
