from rest_framework import serializers
from .models import Property, Reservation
from useraccount.serializers import UserDetailSerializer

# Serializer for the list view of properties
class PropertiesListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'price_per_night',
            'image_url',
            'state',
            'city',
        )

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return None

# Serializer for the detailed view of a property
class PropertiesDetailSerializer(serializers.ModelSerializer):
    landlord = UserDetailSerializer(read_only=True, many=False)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'description',
            'price_per_night',
            'image_url',
            'bedrooms',
            'bathrooms',
            'guests',
            'state',
            'city',
            'landlord'
        )

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return None

# Serializer for the list view of reservations
class ReservationsListSerializer(serializers.ModelSerializer):
    property = PropertiesListSerializer(read_only=True, many=False)
    
    class Meta:
        model = Reservation
        fields = (
            'id', 
            'start_date', 
            'end_date', 
            'number_of_nights', 
            'total_price', 
            'property'
        )
