from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=120, default='password', blank=False, null=False)

	def __unicode__(self):
		return self.email

class Book(models.Model):
	isbn = models.CharField(max_length=13, unique=True)
	rawjson = models.CharField(max_length=100000)

	def __unicode__(self):
		return self.isbn

	def get_isbn(self):
		return self.isbn

	def get_json(self):
		import json
		return json.loads(self.rawjson)

	def title(self):
		try:
			data = self.get_json()
			return data['items'][0]['volumeInfo']['title']
		except:
			return "no title"

	def description(self):
		try:
			data = self.get_json()
			return data['items'][0]['volumeInfo']['description']
		except:
			return "no description"

	def year(self):
		try:
			data = self.get_json()
			return data['items'][0]['volumeInfo']['publishedDate']
		except:
			return "no year"

	def subtitle(self):
		try:
			data = self.get_json()
			return data['items'][0]['volumeInfo']['subtitle']
		except:
			return "no subtitle"

	def authors(self):
		try:
			data = self.get_json()
			return ", ".join(data['items'][0]['volumeInfo']['authors'])
		except:
			return "no authors"

	def cover(self):
		try:
			data = self.get_json()
			return data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
		except:
			return "no cover"