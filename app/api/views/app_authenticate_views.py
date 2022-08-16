from rest_framework import generics
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from app.api.auth.auth import Auth

from app.api.serializers.app_access_token_serializer import AppAccessTokenSerializer
from app.models import App


class AppAuthenticateView(generics.GenericAPIView):
    """ Returns app's payment credentials

    Args:
        generics (GenericAPIView): GenericAPIView

    Returns:
        Response: App payment gateway's credentials
    """
    throttle_classes = [UserRateThrottle]
    serializer_class = AppAccessTokenSerializer

    def post(self, request):
        """Get Access Token For App Using Username And Password

        Args:
            request (request): django request

        Returns:
            list: list of serialized payment credentials
        """
        app = App.objects.filter(username=request.data['username']).first()
        if not app:
            return Response({
                'status': False,
                'error': 'Username or Password Incorrect'
            }, 401)
        auth = Auth(request, App)

        if not auth.match_password(request.data['password'], app.password):
            return Response({
                'status': False,
                'error': 'Username or Password Incorrect'
            }, 401)

        access_token = auth.generate_access_token(app, {})
        return Response({
            'status': True,
            "data": access_token
        }, 200)
