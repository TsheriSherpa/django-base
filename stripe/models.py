from enum import Enum
from django.db import models
from app.models import App
from stripe.api.serializers.credential_serializer import CredentialSerializer


class TransactionStatus(Enum):
    INITIATED = "INITIATED"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    ERROR = "ERROR"

    @classmethod
    def choices(cls) -> tuple:
        return tuple((i.name, i.value) for i in cls)


class Transaction():
    def isSuccess(self) -> bool:
        return True if self.transaction_status == TransactionStatus.COMPLETED else False


class Stripe(models.Model, Transaction):
    app = models.ForeignKey(App, on_delete=models.RESTRICT)
    reference_id = models.CharField(max_length=255, unique=True)
    transaction_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    transaction_status = models.CharField(
        max_length=255, choices=TransactionStatus.choices())
    status_code = models.CharField(max_length=10)
    remarks = models.CharField(max_length=255)
    transaction_date = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=255, null=True)
    request_ip = models.CharField(max_length=255, null=True)
    user_agent = models.CharField(max_length=255, null=True)
    is_test = models.BooleanField(
        default=False, verbose_name="Is test payment?")
    meta_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StripeCredential(models.Model):
    app = models.ForeignKey(App, on_delete=models.RESTRICT)
    base_url = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255)
    publishable_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def serialize(self):
        return CredentialSerializer(self).data
