from django.conf.urls import url
from django.contrib import admin
from .views import RemarkView
from .views import show_remark

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', RemarkView.as_view(), name = "remark_details"),
    url(r'^(?P<remark_id>\d+)/like/$', show_remark),
]
