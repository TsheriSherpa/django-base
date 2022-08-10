from app.api.services.app_services import AppService
from esewa.api.services.esewa_service import EsewaService
from rest_framework import generics
from app.api.permissions.authenticated_app import IsAuthenticatedApp
from rest_framework.throttling import UserRateThrottle
from utils.api_service import ApiService
from utils.helpers import get_client_ip
from rest_framework.response import Response

class EsewaPaymentView(generics.GenericAPIView):
    """ View for payment payhment

    Args:
        generics (GenericAPIView): GenericAPIView

    Returns:
        Response: Whether payment is success or not
    """

    authentication_classes=[IsAuthenticatedApp]
    throttle_classes=[UserRateThrottle]

    service=None

    def __init__(self) -> None:
        super().__init__()
        self.service=EsewaService()

    def get(self,request):
        print(request.app)
        """Get List Of Payment Available For App

        Args:
            request (request): django request

        Returns:
            list:
        """

        log=self.service.create_transaction_log(
            request.app,
            request.GET['credential_type'],
            request.GET['environment'],
            request.GET['amount'],
            request.GET['reference_id'],
            "get_client_ip(request)",
            request.META['HTTP_USER_AGENT'],
            request.GET['remarks'],
            request.GET
        )

        credential=AppService.get_credential(request.app,'esewa',request.GET['credential_type'],request.GET['environment'])
        return self.service.payment_transaction(request,credential,request.GET)

        # return Response({
        #     'status':True if response.status_code == 200 else False,
        #     'data':response
        # },response.status_code)