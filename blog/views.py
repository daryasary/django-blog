from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from blog.models import Post, Category, Tag, Comment
from blog.forms import CommentForm

# Create your views here.
def blog_list(request , cat=None, tag=None, year=None, Month=None):
	Context = {}
	posts = Post.objects.all()
	Categories = Category.objects.all()
	Tags = Tag.objects.all()


	if cat is not None:
		cat = get_object_or_404(Category, slug=cat)
		posts = posts.filter(cat=cat)


	if tag is not None:
		tag = get_object_or_404(Tag, slug=tag)
		posts = posts.filter(tag=tag)

	# Filter posts by date not emplemented yet

	Context['posts'] = posts
	Context['Categories'] = Categories
	Context['Tags'] = Tags

	return render(request, "blog/blog_list_display.html", Context)

def single_post(request, slug):
	# here will retrieve context, 
	# and then render the page
	comment = CommentForm()
	Context = {}
	Categories = Category.objects.all()
	Tags = Tag.objects.all()
	post = get_object_or_404(Post, slug=slug)
	Context['post'] = post
	Context['Categories'] = Categories
	Context['Tags'] = Tags
	Context['Comment'] = comment
	return render(request, 'blog/single_post.html', Context)