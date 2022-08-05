""" Khalti Utilty Class """


import requests
from datetime import datetime
from khalti.models import KhaltiCredential, KhaltiTransaction
from stripe.models import TransactionStatus
from utils.api_service import ApiService


class KhaltiService(ApiService):
    """
        Khalti Utility Class

        Extends (ApiService)
    """

    @classmethod
    def verify_transaction(cls, credential: KhaltiCredential, reference_id: str):
        """ Verify Khalti Transaction

        Args:
            credential (KhaltiCredential): App khalti's Credential
            reference_id (str): Unique id of transaction

        Returns:
            KhaltiTransaction: Khalti transaction log
        """
        url = credential.base_url + "api/v2/payment/verify/"
        payload = {
            "token": reference_id,
            "amount": 1000
        }
        headers = {
            "Authorization": "Key " + credential.secret_key
        }
        return requests.post(url, payload, headers=headers)

    @classmethod
    def create_transaction_log(cls, app, credential_type, environment, amount, reference_id, request_ip, user_agent, remarks):
        """Create Khalti Transaction Log

        Args:
            app (App): App Object
            enviornment (str): test or live?
            data (dict): request's data
        """
        return KhaltiTransaction.objects.create(
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
            is_test=True if environment == "test" else False
        )

    @classmethod
    def update_transaction_log(cls, log: KhaltiTransaction, response):
        """Update Khalti Transaction Log

        Args:
            log (KhaltiTransaction): log object
            response (Object): requests.Response object

        Returns:
            void: return nothing
        """
        success = True if response.status_code == 200 else False
        if success:
            log.transaction_id = response.idx

        log.status_code = "00" if success else "01",
        log.customer_name = response.user.name if success else None,
        log.customer_phone = response.user.mobile if success else None,
        log.meta_data = response.json()
        log.save()
