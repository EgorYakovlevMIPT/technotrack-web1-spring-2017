from django.shortcuts import  render
from django.shortcuts import HttpResponse, HttpResponseRedirect

def load_main(request):

	return render(request, 'file.html')

def load_profile_list(request):

	return render(request, 'profile_list.html')