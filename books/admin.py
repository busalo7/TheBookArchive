from django.contrib import admin

# Register your models here.
from .models import Book, Page
admin.site.register(Book)
admin.site.register(Page)
