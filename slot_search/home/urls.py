from django.conf.urls import url, include

from home.views import  MainPage,  do_empty, do_start
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="home/slot_finder.html")),
    # url(r'^$', TemplateView.as_view(template_name="home/ index.html")),
    url(r'^$', MainPage.as_view(), name="main_page"),
    url(r'^do-empty/$', do_empty, name="do_empty"),
    url(r'^do-start/$', do_start, name="do_start"),
]