class createbook:
	def __init__(self, isbn):
		self.isbn = isbn

	def make(self):
		from .models import Book
		return Book(isbn=self.isbn, rawjson=self.get_rawjson())

	def get_rawjson(self):
		import urllib
		return urllib.urlopen(self.gen_url()).read()

	def gen_url(self):
		return "https://www.googleapis.com/books/v1/volumes?q=isbn:" + self.isbn

