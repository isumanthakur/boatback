from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from property.models import Property
from .models import Review
from .serializers import ReviewSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def create_review(request, property_id):
    try:
        property = Property.objects.get(id=property_id)
    except Property.DoesNotExist:
        return Response({"error": "Property not found"}, status=status.HTTP_404_NOT_FOUND)
    
    user = request.user
    data = {
        'property': property.id,
        'star_rating': request.data.get('star_rating'),
        'comment': request.data.get('comment'),
    }
    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=user)  # Pass the user here
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def property_reviews(request, property_id):
    try:
        property = Property.objects.get(id=property_id)
    except Property.DoesNotExist:
        return Response({"error": "Property not found"}, status=status.HTTP_404_NOT_FOUND)
    
    reviews = property.reviews.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)
