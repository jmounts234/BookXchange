from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='overview'),
  url(r'^overview/$', views.overview, name='overview'),
  url(r'^signUp/$', views.signUp, name='signUp')
]