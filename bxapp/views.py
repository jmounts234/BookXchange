from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from django.shortcuts import render_to_response

def index(request):
	return allBooks(request)

def allBooks(request):

	import urllib, json
	url = "https://www.googleapis.com/books/v1/volumes?q=isbn:9780321534965"
	response = urllib.urlopen(url)
	bookinfo = json.loads(response.read())
	title = bookinfo['items'][1]['volumeInfo']['title']


	template = loader.get_template('books_overview.html')
	context = RequestContext(request, {"title" : title})
	return HttpResponse(template.render(context))

def indiviualBooks(request):
	template = loader.get_template('books_specview.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def signUp(request):
	template = loader.get_template('signup.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))