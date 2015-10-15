from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from .models import *

def index(request):
	return overview(request)

def overview(request):
	# from .helpers import createbook
	# createbook('9780553293357').make()
	# createbook('9780131103627').make()
	
	try:
		books = Book.objects.all()
		template = loader.get_template('overview.html')
		context = RequestContext(request, { 'books' : books })
		return HttpResponse(template.render(context))
	except:
		return HttpResponse("The book you've selected does not exist.")

def signUp(request):
	template = loader.get_template('signup.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))