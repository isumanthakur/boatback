from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    # Nested user information for reviews
    user = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'property', 'star_rating', 'comment', 'user', 'created_at']  # Include 'user' here
        read_only_fields = ['user', 'created_at']  # 'user' should be read-only

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "name": obj.user.name,
            "avatar_url": obj.user.avatar_url()
        }
