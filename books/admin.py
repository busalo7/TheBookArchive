from django.contrib import admin

# Register your models here.
from .models import Book, Page, BookRating
admin.site.register(Book)
admin.site.register(Page)

admin.site.register(BookRating)
