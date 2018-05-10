from django.shortcuts import render
from .serializers import BookListSerializer,  BookDetailSerializer, BookCreateSerializer, PageCreateSerializer, UserCreateSerializer, BookRatingCreateSerializer, UserLoginSerializer, FavoriteCreateSerializer, CommentCreateSerializer
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from books.models import Book, Page, Profile, FavoriteBook, Comment,BookRating
from django.contrib.auth.models import User
import json
import base64


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

'''class PageCreateAPIView(APIView):
    serializer_class = PageCreateSerializer

    def post(self, request):
        img_data = base64.b64decode(request.data.get("base64"))
        print (img_data)
        filename = "page_image.gif"
        print (filename)
        with open(filename, 'wb') as f:
            f.write(img_data)
        print (filename)
        data = {
            "base64": request.data.get("base64"),
            "book": request.data.get("book"),
            "page_text": request.data.get("page_text"),
            "page_image":filename
        }
        serializer = PageCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            print ("YAY")'''



class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class LoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        my_data = request.data
        my_serializer = UserLoginSerializer(data=my_data)
        if my_serializer.is_valid(raise_exception=True):
            new_data = my_serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(my_serializer.errors, status=HTTP_400_BAD_REQUEST)

class FavoriteCreateView(CreateAPIView):
    queryset = FavoriteBook.objects.all()
    serializer_class = FavoriteCreateSerializer

class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

class BookRatingCreateView(CreateAPIView):
    queryset = BookRating.objects.all()
    serializer_class = BookRatingCreateSerializer
