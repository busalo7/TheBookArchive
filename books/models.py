from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	book_name   = models.CharField()
	cover_image = models.ImageField(null=True)
	book_description = models.TextField(max_length=300, null=True)
	

	def __str__(self):
		return self.book_name

# Create your models here.
