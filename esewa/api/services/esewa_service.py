import requests
from esewa.models import EsewaCredential, EsewaTransaction
from utils.api_service import ApiService
from stripe_card.models import TransactionStatus
from datetime import datetime
from utils.helpers import dict_get_value
from django.shortcuts import get_object_or_404, redirect, render

class EsewaService(ApiService):
    """
    Esewa utility class

    Extends (ApiService)
    """

    def payment_transaction(self,request, credential: EsewaCredential, data):
        """ Verify Khalti Transaction

        Args:
            credential (EsewaCredential): App esewa's Credential
            reference_id (str): Unique id of transaction

        Returns:
            EsewaCredential: Esewa transaction log
        """
        # print("credential-----------------------",credential)
        url = credential.base_url+"epay/main/"
        # print(url)
        payload = {
            'amt': data['amount'],
            'pdc': 0,
            'psc': 0,
            'txAmt': 0,
            'tAmt': 100,
            'pid': data['reference_id'],
            'scd': credential.secret_key,
            'su': credential.success_url,
            'fu': credential.failure_url,
            'url':url
        }
        print("=============",payload)
        return render(request,'esewa/index.html',payload) 

        # return requests.post(url,payload)

    @classmethod
    def create_transaction_log(cls, app, credential_type, environment, amount, reference_id, request_ip, user_agent, remarks, request_data):
        return EsewaTransaction.objects.create(
            app=app,
            amount=amount,
            meta_data={},
            remarks=remarks,
            status_code="01",
            user_agent=user_agent,
            request_ip=request_ip,
            reference_id=reference_id,
            transaction_date=datetime.now(),
            credential_type=credential_type,
            transaction_status=TransactionStatus.INITIATED,
            is_test=True if environment == "test" else False,
            customer_name=dict_get_value("name", request_data),
            customer_phone=dict_get_value("phone", request_data),
            customer_email=dict_get_value("email", request_data),
        )

