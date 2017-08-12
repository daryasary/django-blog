from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language, get_language_from_request

from blog.models import Post, Category, Tag
from blog.forms import CommentForm


def blog_list(request, cat=None, tag=None, year=None, Month=None):
    context = {}
    lang = get_language_from_request(request)
    posts = Post.objects.filter(lang=lang)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if cat is not None:
        cat = get_object_or_404(Category, slug=cat)
        posts = posts.filter(cat=cat)

    if tag is not None:
        tag = get_object_or_404(Tag, slug=tag)
        posts = posts.filter(tag=tag)

    # Filter posts by date not emplemented yet

    context['posts'] = posts
    context['Categories'] = categories
    context['Tags'] = tags

    return render(request, "blog/blog_list_display.html", context)


def single_post(request, slug):
    comment = CommentForm()
    context = {}
    categories = Category.objects.all()
    tags = Tag.objects.all()
    post = get_object_or_404(Post, slug=slug)
    context['post'] = post
    context['Categories'] = categories
    context['Tags'] = tags
    context['Comment'] = comment
    return render(request, 'blog/single_post.html', context)
