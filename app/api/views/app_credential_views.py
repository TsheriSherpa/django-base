from rest_framework import generics
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from app.api.permissions.authenticated_app import IsAuthenticatedApp
from stripe.models import StripeCredential


class AppCredentialView(generics.GenericAPIView):
    """ Returns app's payment credentials

    Args:
        generics (GenericAPIView): GenericAPIView

    Returns:
        Response: App payment gateway's credentials
    """
    authentication_classes = [IsAuthenticatedApp]
    throttle_classes = [UserRateThrottle]

    def get(self, request):
        """Get List Of Payment Available For Given App Id

        Args:
            app_id (int): id of app

        Returns:
            list: list of serialized payment credentials
        """
        payment_credentials = []
        stripe = StripeCredential.objects.filter(
            app_id=request.app.id).first().serialize()

        if stripe:
            payment_credentials.append(stripe)

        return Response({
            'status': True,
            "data": payment_credentials
        }, 200)
