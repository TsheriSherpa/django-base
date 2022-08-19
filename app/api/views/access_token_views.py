from rest_framework import generics
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from app.models import App
from app.api.auth.auth import Auth
from app.api.serializers.app_access_token_serializer import AppAccessTokenSerializer
from utils.helpers import get_error_message


class AccessTokenView(generics.GenericAPIView):
    """ Generate Access Token From Refresh Token

    Args:
        generics (GenericAPIView): GenericAPIView

    Returns:
        Response: Access Token
    """
    throttle_classes = [UserRateThrottle]
    serializer_class = AppAccessTokenSerializer

    def post(self, request):
        """Get Access Token For App Using Refresh Token

        Args:
            request (request): django request

        Returns:
            dict: access_token and refresh_token
        """

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "status": False,
                "error": get_error_message(serializer)
            }, 422)

        auth = Auth(request,  App)
        try:
            app = auth.app_from_refresh_token()
        except Exception:
            return Response({
                'status': False,
                'error': 'Invalid Refresh Token'
            })

        if not app:
            return Response({
                'status': False,
                'error': 'Invalid Refresh Token'
            })

        token = auth.generate_access_token(
            app, {}, request.data['refresh_token'])

        return Response({
            'status': True,
            'data': token
        }, 200)
