from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post, Category, Tag, Comment

# Create your views here.
def blog_list(request):
	Context = {}
	posts = Post.objects.all()
	Context['posts'] = posts

	categories = Category.objects.all()
	Context['categories'] = categories

	tags = Tag.objects.all()
	Context['tags'] = tags

	return render(request, "blog/blog_list_display.html", Context)

def single_post(request, slug):
	# here will retrieve context, 
	# and then render the page
	try:
		post = Post.objects.get(slug=slug)
		# return HttpResponse( 'good request for %s' %post_id)
		return render(request, 'blog/single_post.html', {'post':post})
	except:
		return HttpResponse('bad requests for %s' %slug)
