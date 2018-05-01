from django.shortcuts import render
from .serializers import *
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView, 
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response

# Create your views here.


class BookListAPIView(ListAPIView):
	queryset = Book.objects.all()
    serializer_class = BookListSerializer