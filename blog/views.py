from django.shortcuts import render

# Create your views here.
def blog_list(request):
	return render(request, "blog/blog_list_display.html")

def single_post(request):
	# here will retrieve context, 
	# and then render th page
	return render(request, 'blog/single_post.html')