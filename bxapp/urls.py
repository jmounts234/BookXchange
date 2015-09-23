from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.allBooks, name='allBooks'),
    url(r'^$', views.individualBook, name='individualBook'),
    url(r'^$', views.signUp, name='signUp'),
]