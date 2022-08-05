from urllib import response
from django.conf import settings
import requests
import json
from app.api.services.app_services import AppService
from khalti.api.serializers.verify_serializers import VerifySerializer
from khalti.api.services.khalti_service import KhaltiService
from khalti.models import KhaltiCredential

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from app.api.permissions.authenticated_app import IsAuthenticatedApp
from khalti.api.serializers.credential_serializer import CredentialSerializer
from utils.helpers import get_client_ip


class KhaltiVerifyView(generics.GenericAPIView):
    """ View for verifying khalti's payment 

    Args:
        generics (GenericAPIView): GenericAPIView

    Returns:
        Response: Whether payment is success or not
    """
    authentication_classes = [IsAuthenticatedApp]
    throttle_classes = [UserRateThrottle]
    serializer_class = VerifySerializer

    def get(self, request):
        """Get List Of Payment Available For App

        Args:
            request (request): django request

        Returns:
            list: 
        """
        log = KhaltiService.create_transaction_log(
            request.app,
            request.GET['credential_type'],
            request.GET['environment'],
            request.GET['amount'],
            request.GET['reference_id'],
            get_client_ip(request),
            request.META['HTTP_USER_AGENT'],
            request.GET['remarks']
        )

        credential = AppService.get_credential(
            request.app, 'khalti', request.GET.get('credential_type'), request.GET.get('environment').upper())

        response = KhaltiService.verify_transaction(
            credential, request.GET.get('reference_id'))

        print(log)
        KhaltiService.update_transaction_log(log, response)

        return Response({
            'status': True if response.status_code == 200 else False,
            'data': response.json()
        }, response.status_code)
