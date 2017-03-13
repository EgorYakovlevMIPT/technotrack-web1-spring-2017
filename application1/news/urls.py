from django.conf.urls import url
from django.contrib import admin
from .views import NewsView
from .views import show_news

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', NewsView.as_view(), name = "news_details"),
    url(r'^(?P<news_id>\d+)/$', show_news),
    url(r'^(?P<news_id>\d+)/like/$', show_news),
]
