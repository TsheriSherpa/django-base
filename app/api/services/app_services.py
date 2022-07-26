
from re import L
from sys import api_version

from khalti.models import KhaltiCredential
from stripe_card.models import StripeCredential


class AppService:
    """ App Utility Class """

    @classmethod
    def get_credential(cls, app, gateway, credential_type, environment):
        if gateway == 'khalti':
            return KhaltiCredential.objects.filter(
                app=app, credential_type=credential_type.upper(), environment=environment.upper()).first()

        if gateway == 'stripe':
            return StripeCredential.objects.filter(
                app=app, credential_type=credential_type.upper(), environment=environment.upper()).first()

        raise Exception("Unknown Payment Gateway")
