from rest_framework import generics
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from app.api.permissions.authenticated_app import IsAuthenticatedApp
from khalti.api.serializers.credential_serializer import CredentialSerializer
from khalti.models import KhaltiCredential
from stripe_card.models import StripeCredential


class AppCredentialView(generics.GenericAPIView):
    """ Returns app's payment credentials

    Args:
        generics (GenericAPIView): GenericAPIView

    Returns:
        Response: App payment gateway's credentials
    """
    authentication_classes = [IsAuthenticatedApp]
    throttle_classes = [UserRateThrottle]
    serializer_class = CredentialSerializer

    def get(self, request):
        """Get List Of Payment Available For App

        Args:
            request (request): django request

        Returns:
            list: list of serialized payment credentials
        """
        payment_credentials = []
        stripe = StripeCredential.objects.filter(
            app_id=request.app.id).first()

        khaltis = KhaltiCredential.objects.filter(
            app_id=request.app.id)

        if stripe:
            payment_credentials.append(stripe.serialize())

        for khalti in khaltis:
            payment_credentials.append(khalti.serialize())

        return Response({
            'status': True,
            "data": payment_credentials
        }, 200)
