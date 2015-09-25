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

	def get_json(self):
		import json
		return json.loads(self.rawjson)

	def title(self):
		data = self.get_json()
		return data['items'][1]['volumeInfo']['title']

	def description(self):
		data = self.get_json()
		return data['items'][2]['volumeInfo']['description']

	def year(self):
		data = self.get_json()
		return data['items'][2]['volumeInfo']['publishedDate']

	def subtitle(self):
		data = self.get_json()
		return data['items'][1]['volumeInfo']['subtitle']

	def authors(self):
		data = self.get_json()
		return ", ".join(data['items'][1]['volumeInfo']['authors'])

	def cover(self):
		data = self.get_json()
		return data['items'][2]['volumeInfo']['imageLinks']['thumbnail']