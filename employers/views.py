from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EmployerSerializer


@api_view(['POST'])
def verify_employer(request):
    serializer = EmployerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
