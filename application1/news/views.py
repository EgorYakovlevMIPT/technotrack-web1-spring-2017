from django.shortcuts import  render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from .models import Article

class NewsView (DetailView):

	model = Article
	template_name = 'article.html'

def show_news(request, news_id = 0, cat_id = 0):
	'''#resp = HttpResponse (u"Category {} Article {}".format(cat_id, news_id))
	resp = HttpResponseRedirect ('http://yandex.ru/')
	return resp'''
	return render(request, 'template_blabla.html', {"news_id": news_id})