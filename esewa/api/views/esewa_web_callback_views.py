from app.api.services.app_services import AppService
from esewa.api.services.esewa_service import EsewaService
from ...models import EsewaTransaction
from rest_framework import generics
from app.api.permissions.authenticated_app import IsAuthenticatedApp
from rest_framework.throttling import UserRateThrottle
from utils.api_service import ApiService
from utils.helpers import get_client_ip
from rest_framework.response import Response

class EsewaWebCallback(generics.GenericAPIView):
    service = None

    def __init__(self) -> None:
        super().__init__()
        self.service = EsewaService()

    def get(self,request,status):
        data=request.GET.get("oid")
        refId=request.GET.get("refId") if request.GET else ""
        log=EsewaTransaction.objects.filter(reference_id=data).first()
        if status=="success":
            self.service.update_transaction_log(log,status,refId,self.service.getErrorMessage)
        else:
            self.service.update_transaction_log(log,status,refId,self.service.getErrorMessage)

        return Response({
            "status":True if status == "success" else False,
            "message":status
        })
