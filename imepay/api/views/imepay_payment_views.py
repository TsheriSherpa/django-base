from rest_framework import generics
from app.api.permissions.authenticated_app import IsAuthenticatedApp
from rest_framework.throttling import UserRateThrottle
from imepay.api.services.imepay_service import ImePayService
from utils.helpers import get_client_ip
from app.api.services.app_service import AppService
from rest_framework.response import Response


class ImepayPaymentView(generics.GenericAPIView):
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
        self.service=ImePayService

    def post(self,request):

        credential=AppService.get_credential(request.app,'imepay',request.data['credential_type'],request.data['environment'])
        token=self.service.fetch_payment_token(request,credential)
        payload=self.service.generate_payload(token,credential,request.data)
        return Response({
            "status":True,
            "data":payload,
            "token":token
        })


        
        # log=self.service.create_transaction_log(
        #     request.app,
        #     request.GET['credential_type'],
        #     request.GET['environment'],
        #     request.GET['amount'],
        #     request.GET['reference_id'],
        #     get_client_ip(request),
        #     request.META['HTTP_USER_AGENT'],
        #     request.GET['remarks'],
        #     request.GET
        # )

    