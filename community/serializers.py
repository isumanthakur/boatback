from rest_framework import serializers
from .models import Post, Like, Comment

class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'image', 'video', 'likes_count', 'comments_count', 'comments', 'created_at', 'updated_at']

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "name": obj.user.name,
            "avatar_url": obj.user.avatar_url(),
        }

    def get_comments(self, obj):
        # Ensure comments is always an array
        return CommentSerializer(obj.comments.all(), many=True).data if obj.comments.exists() else []

    
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'text', 'created_at']

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "name": obj.user.name,
            "avatar_url": obj.user.avatar_url(),
        }
