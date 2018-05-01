from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'description']
