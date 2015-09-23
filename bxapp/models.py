from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	password = CharField(max_length=120, default='password', blank=False, null=False)

	def __unicode__(self):
		return self.email