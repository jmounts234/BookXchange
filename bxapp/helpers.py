class createbook:
	def __init__(self, isbn):
		isbn2 = "".join([n for n in isbn if n in "1234567890X"])
		self.isbn = isbn2

	def validate_isbn(self):
		if len(self.isbn) == 13 or len(self.isbn) == 10: return True 
		return False

	def validate_json(self):
		import json
		data = json.loads(self.get_rawjson())
		if data['totalItems'] == 0: return False
		return True

	def make(self):
		if not self.validate_isbn(): return False
		from .models import Book
		book = Book(isbn=self.isbn, rawjson=self.get_rawjson())
		if not self.validate_json(): return False
		book.save()
		return book

	def get_rawjson(self):
		import urllib
		return urllib.urlopen(self.gen_url()).read()

	def gen_url(self):
		return "https://www.googleapis.com/books/v1/volumes?q=isbn:" + self.isbn

class createuser:
	def __init__(self, email, password):
		self.email = email
		self.password = password

	def signUp(self):
		from .models import User
		user = User(email = self.email, password = self.password)
		user.save()
		return user