from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User , on_delete=models.CASCADE)
	profile_image = models.ImageField()
	profile_bio = models.TextField(max_length=300, null=True)



class Book(models.Model):
	book_name   = models.CharField(max_length=20)
	cover_image = models.ImageField(null=True)
	book_description = models.TextField(max_length=300, null=True)
	

	def __str__(self):
		return self.book_name

# Create your models here.

class Page(models.Model):
	page_image = models.ImageField()
	page_text = models.TextField()
	book = models.ForeignKey(Book, on_delete=models.CASCADE)

