from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication  # Use JWT Authentication
from razorpay import Client
from .models import Payment
from property.models import Property
from django.conf import settings

# Initialize Razorpay client
razorpay_client = Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_SECRET_KEY))

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def create_payment(request, property_id):
    # Check if the property exists
    try:
        property = Property.objects.get(id=property_id)
    except Property.DoesNotExist:
        return Response({"error": "Property not found"}, status=status.HTTP_404_NOT_FOUND)
    
    user = request.user
    amount = int(property.price_per_night * 100)  # Convert amount to paise

    try:
        # Create Razorpay order
        razorpay_order = razorpay_client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1',
        })

        # Save Payment object
        payment = Payment.objects.create(
            user=user,
            property=property,
            amount=amount / 100,  # Store amount in Rupees
            payment_id=razorpay_order['id'],
            payment_status='CREATED',
        )

        # Return the response with Razorpay order details
        return Response({
            'razorpay_order_id': razorpay_order['id'],
            'razorpay_key': settings.RAZORPAY_API_KEY,
            'amount': amount,
            'currency': 'INR',
            'property_id': str(property.id),
        }, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def payment_success(request):
    try:
        # You can implement your logic here to verify payment, update status, etc.
        # For now, we'll just return a success response
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
