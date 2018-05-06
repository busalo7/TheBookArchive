from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from books.models import Book, Page, Profile, FavoriteBook, Comment,BookRating
from django.http import JsonResponse



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    pages = serializers.SerializerMethodField()
    favs = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'

    def get_pages(self, obj):
        pages = obj.page_set.all()
        json_pages = PageListSerializer(pages, many=True).data
        return json_pages


    def get_favs(self, obj):
        favs = obj.favoritebook_set.all()
        json_favs = FavoriteListSerializer(favs, many=True).data
        return json_favs

    def get_comments(self, obj):
        comments = obj.comment_set.all()
        json_comments = CommentListSerializer(comments, many=True).data
        return json_comments


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


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    def validate(self, data):
        my_username = data.get('username')
        my_password = data.get('password')

        if my_username == '':
            raise serializers.ValidationError(" A username is required to login ")

        try:
            user_obj = User.objects.get(username=my_username)
        except:
            raise serializers.ValidationError(" A username does not exist ")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError(" Incorrect username/password combination ")

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)

        data["token"] = token


        return data
class BookRatingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRating
        fields = '__all__'


class FavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteBook
        fields = ['book']

class FavoriteListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = FavoriteBook
        fields = ['user']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['book']

class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['user']
