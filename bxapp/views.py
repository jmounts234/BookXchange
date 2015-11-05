from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from .models import *
from .helpers import *

def index(request):
	return overview(request)

def overview(request):
	if(request.GET.get('purchase')):
		context = RequestContext(request, {})
		isbnToRemove = request.GET.get('isbn')
		book = Book.objects.get(isbn = isbnToRemove)
		book.delete()
		template = loader.get_template('purchase.html')
		return HttpResponse(template.render(context))

	try:
		mail = request.COOKIES['mail']
	except:
		mail = None

	try:
		books = Book.objects.all()
		template = loader.get_template('overview.html')
		context = RequestContext(request, { 'books' : books, 'name' : mail }) 
		return HttpResponse(template.render(context))
	except:
		return HttpResponse("The page you've selected does not exist.")

def signUp(request):
	if(request.GET.get('signUp')):
		email = request.GET.get('email')
		password = request.GET.get('password')	
		try:
			createuser(email, password).signUp()
		except:
			return HttpResponse("User name is already in use.")
		return HttpResponseRedirect('/')
	else:
		template = loader.get_template('signup.html')

	context = RequestContext(request, {})
	return HttpResponse(template.render())

def signin(request):
	context = RequestContext(request, {})

	if(request.GET.get('signin')):
		aemail = request.GET.get('email')
		apassword = request.GET.get('password')
		try:
			User.objects.get(email = aemail, password = apassword)
			template = loader.get_template('overview.html')
			response = HttpResponseRedirect('/')
			response.set_cookie('mail', aemail, max_age = 100000000)
		except:
			return HttpResponse("The username/pass does not exist.")
	else:
		template = loader.get_template('signin.html')
		return HttpResponse(template.render(context))

	return response

def logout(request):
  response = HttpResponseRedirect('/')
  response.delete_cookie('mail')
  return response

def purchase(request):
	context = RequestContext(request, {})
	template = loader.get_template('purchase.html')
	return HttpResponse(template.render(context))

def addBook(request):
	try:
		mail = request.COOKIES['mail']
	except:
		mail = None
		return HttpResponseRedirect('/')

	context = RequestContext(request, {'name' : mail })
	if(request.GET.get('addBook')):
		isbn = request.GET.get('isbn')
		try:
			if not createbook(isbn).make():
				return HttpResponse("Invalid ISBN number.")
			template = loader.get_template('overview.html')
			return HttpResponseRedirect('/')
		except:
			return HttpResponse("ISBN already exists")
	else:
		template = loader.get_template('addBook.html')

	return HttpResponse(template.render(context))



