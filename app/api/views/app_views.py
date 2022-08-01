from rest_framework import generics, serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response


class AppView(generics.GenericAPIView):
    # permission_class = [AllowAny]
    throttle_classes = [UserRateThrottle]

    @api_view(['GET'])
    def get_credentials(request):
        return Response({
            'status': True,
            "data": []
        }, 200)
