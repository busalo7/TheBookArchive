from django.shortcuts import render
from .serializers import BookListSerializer,  BookDetailSerializer, BookCreateSerializer, PageCreateSerializer, UserCreateSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from books.models import Book, Page, Profile
from django.contrib.auth.models import User


# Create your views here.


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'page_id'

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    
    
class PageCreateAPIView(CreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageCreateSerializer
    
    
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer