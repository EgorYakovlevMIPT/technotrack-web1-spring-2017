from django.shortcuts import  render
from django.views.generic import DetailView
from .models import Remark

class RemarkView (DetailView):

	model = Remark
	template_name = 'remark.html'

def show_remark(request, remark_id = 0):
	'''#resp = HttpResponse (u"Category {} Article {}".format(cat_id, news_id))
	resp = HttpResponseRedirect ('http://yandex.ru/')
	return resp'''
	return render(request, 'template_blabla.html', {"remark_id": remark_id})