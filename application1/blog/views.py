from django.shortcuts import  render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Blog

class BlogView (ListView):

	model = Blog
	template_name = 'blog.html'

class BlogList (ListView):

	model = Blog
	template_name = 'blog_list.html'

def show_blog(request, blog_id = 0):
	return render(request, 'templates_blabla.html', {"blog_id": blog_id})