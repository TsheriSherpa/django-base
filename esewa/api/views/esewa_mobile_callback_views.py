from fcntl import F_ADD_SEALS
from app.api.services.app_services import AppService
from esewa.api.services.esewa_service import EsewaService
from ...models import EsewaTransaction
from rest_framework import generics
from app.api.permissions.authenticated_app import IsAuthenticatedApp
from rest_framework.throttling import UserRateThrottle
from utils.api_service import ApiService
from utils.helpers import get_client_ip
from rest_framework.response import Response


class EsewaMobileCallback(generics.GenericAPIView):
    service = None

    def __init__(self) -> None:
        super().__init__()
        self.service = EsewaService()

    def post(self, request):
        if EsewaTransaction.objects.filter(reference_id=request.data['transactionDetails']['referenceId']).exists():
            return Response({
                "status":False,
                "message":"Reference aready used"
            },422)
        else:
            log=self.service.create_transaction_log(
                request.data['app'] if 'app' in request.data else None,
                request.data['credential_type'] if 'credential_type' in request.data else '',
                request.data['environment'] if 'environment' in request.data else '',
                request.data['totalAmount'],
                request.data['transactionDetails']['referenceId'],
                get_client_ip(request),
                request.META['HTTP_USER_AGENT'],
                request.data['remarks'] if 'remarks' in request.data else '',
                request.data  
            )
    
        return Response({
            "status": True if request.data['transactionDetails']['status']=="COMPLETE" else False,
            "message": request.data['message']['technicalSuccessMessage'] 
        })
