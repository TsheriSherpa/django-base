from enum import Enum
from django.db import models
from app.models import App
from stripe.models import Transaction, TransactionStatus

from khalti.api.serializers.credential_serializer import CredentialSerializer


class KhaltiTransaction(models.Model, Transaction):
    app = models.ForeignKey(App, on_delete=models.RESTRICT)
    reference_id = models.CharField(max_length=255, unique=True)
    transaction_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    transaction_status = models.CharField(
        max_length=255, choices=TransactionStatus.choices())
    status_code = models.CharField(max_length=10)
    remarks = models.CharField(max_length=255)
    transaction_date = models.DateTimeField(auto_now_add=True)
    customer_email = models.CharField(max_length=255, null=True)
    request_ip = models.CharField(max_length=255, null=True)
    user_agent = models.CharField(max_length=255, null=True)
    is_test = models.BooleanField(
        default=False, verbose_name="Is test payment?")
    customer_name = models.CharField(max_length=255, null=True)
    customer_phone = models.CharField(max_length=15, null=True)
    meta_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class KhaltiCredential(models.Model):
    app = models.ForeignKey(App, on_delete=models.RESTRICT)
    base_url = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255)
    public_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def serialize(self):
        return CredentialSerializer(self).data
