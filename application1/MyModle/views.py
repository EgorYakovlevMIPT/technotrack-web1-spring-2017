from django.shortcuts import  render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Profile

class ModleView (DetailView):

	model = Profile
	template_name = 'profile.html'

class ModelList (ListView):

	template_name = 'profile_list.html'
	model = Profile

def show_modle(request, modle_id = 0):
	return render(request, 'template_blabla.html', {"modle_id": modle_id})