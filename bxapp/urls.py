from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^books/$', views.allBooks, name='allBooks'),
    url(r'^books/individual/$', views.indiviualBooks, name='indiviualBooks'),
    url(r'^signup/$', views.signUp, name='signUp'),

]