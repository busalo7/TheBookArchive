"""arabeyes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from api.views import BookListAPIView, BookDetailAPIView, BookCreateAPIView, PageCreateAPIView,  UserCreateAPIView, LoginAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/list/', BookListAPIView.as_view()),
    path('api/detail/<int:page_id>/', BookDetailAPIView.as_view(), name="api_detail"),
    path('api/create/', BookCreateAPIView.as_view()),
    path('api/page_create/', PageCreateAPIView.as_view()),
    path('api/register/', UserCreateAPIView.as_view(), name='api_register'),
    path('api/login/', LoginAPIView.as_view(), name='api_login'),


   ]
