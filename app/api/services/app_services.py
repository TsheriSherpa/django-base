
from re import L
from sys import api_version

from khalti.models import KhaltiCredential
from stripe.models import StripeCredential


class AppService:
    """ App Utility Class """

    @classmethod
    def get_credential(cls, app, gateway, credential_type, environment):
        if gateway == 'khalti':
            return KhaltiCredential.objects.filter(
                app=app, credential_type=credential_type, environment=environment).first()

        if gateway == 'stripe':
            return StripeCredential.objects.filter(
                app=app, credential_type=credential_type, environment=environment).first()

        raise Exception("Unknown Payment Gateway")
