from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SubscriptionSerializer
from .models import Subscription


@api_view(['POST'])
def subscriber(request):
    serializer = SubscriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def resubscriber(request):
    try:
        subscriber = Subscription.objects.get(email=request.data['email'])
        subscriber.is_active = True
        subscriber.save()
    except Subscription.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def unsubscriber(request):
    try:
        subscriber = Subscription.objects.get(email=request.data['email'])
        subscriber.delete()
    except Subscription.DoesNotExist as e:
        return Response({'error': 'email not subscribed'}, status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_200_OK)
