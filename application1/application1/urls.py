from django.conf.urls import url, include
from django.contrib import admin
from .views import load_main
from .views import load_profile_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', load_main),
    url(r'^news/', include ('news.urls')),
    url(r'profile_list/', include ('MyModle.urls')),
    url(r'^remark/', include ('comment.urls')),
    url(r'^blog_list/', include ('blog.urls')),
    url(r'^profile/', include ('MyModle.urls')),
]
