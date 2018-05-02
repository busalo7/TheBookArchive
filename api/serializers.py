from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from books.models import Book, Page, Profile
from django.http import JsonResponse 


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    pages = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'

    def get_pages(self, obj):
        pages = obj.page_set.all()
        json_pages = PageListSerializer(pages, many=True).data
        return json_pages

class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class PageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()

        new_profile = Profile(user=new_user)
        new_profile.save()

        return validated_data


