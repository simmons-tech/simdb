from django.conf.urls import url
from people import views

urlpatterns = [
    url(r'^$', views.directory, name='directory'),
    url(r'^entry/(?P<username>[a-z]*)$', views.entry, name='directory_entry'),
]
