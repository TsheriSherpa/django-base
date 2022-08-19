from rest_framework import generics
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from drf_yasg.utils import swagger_auto_schema

from app.api.permissions.authenticated_app import IsAuthenticatedApp
from prabhupay.api.serializers.web_payment_serializers import WebPaymentSerializer
from prabhupay.api.services.PrabhupayService import PrabhupayService
from utils.api_response import ApiResponse
from utils.helpers import get_error_message


class WebPaymentView(generics.GenericAPIView):
    """ Make Payment From Prabhupay Through Web Channel

    Args:
        generics (GenericAPIView): GenericAPIView

    Returns:
        Response: Access Token
    """
    throttle_classes = [UserRateThrottle]
    serializer_class = WebPaymentSerializer
    authentication_classes = [IsAuthenticatedApp]

    def __init__(self):
        super().__init__()
        service = PrabhupayService()

    @swagger_auto_schema(
        request_body=WebPaymentSerializer,
        responses={
            200: WebPaymentSerializer
        }
    )
    def post(self, request):
        """Make payment from prabhupay web channel

        Args:
            request (request): django request

        Returns:
            dict: 
        """

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return ApiResponse.send_error(get_error_message(serializer), 400)

        return Response({
            'status': True,
            'data': 'success'
        }, 200)
