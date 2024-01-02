from rest_framework import serializers
from core.models import Post, Comment, Notification
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    class Meta:
        model = Post
        fields = ['title', 'read', 'category', 'author']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset= Post.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset= Comment.objects.all())
    notifications = serializers.PrimaryKeyRelatedField(many=True, queryset= Notification.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments', 'notifications']