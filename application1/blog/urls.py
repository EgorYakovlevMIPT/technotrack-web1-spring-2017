from django.conf.urls import url
from django.contrib import admin
from .views import BlogView
from .views import BlogList

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name = "blog_details"),
    url(r'$', BlogList.as_view(), name = "blog_list"),
]