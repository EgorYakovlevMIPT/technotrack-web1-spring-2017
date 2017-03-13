from django.conf.urls import url
from django.contrib import admin
from .views import ModleView
from .views import show_modle
from .views import ModelList

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ModleView.as_view(), name = "modle_details"),
    url(r'$', ModelList.as_view(), name = "profile_list"),
]
