from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from django.shortcuts import render_to_response

def index(request):
	return allBooks(request)

def allBooks(request):
	template = loader.get_template('books_overview.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def indiviualBooks(request):
	template = loader.get_template('books_specview.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def signUp(request):
	template = loader.get_template('signup.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))