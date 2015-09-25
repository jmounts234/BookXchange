from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^$', views.overview, name='overview'),
    url(r'^$', views.book, name='book'),
    url(r'^signup/$', views.signUp, name='signUp'),

]