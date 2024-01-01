from rest_framework import serializers
from core.models import Post, Comment, Notification
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

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