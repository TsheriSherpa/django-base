from datetime import datetime
from sre_constants import SUCCESS
import stripe
from utils.api_service import ApiService
from stripe_card.models import StripeTransaction, TransactionStatus
from utils.helpers import dict_get_value


class StripeService(ApiService):
    """Stripe Service Class

    Extends:
        ApiService (Class): Extends ApiService Class
    """

    @classmethod
    def create_transaction_log(cls, app, credential_type, environment, amount, charge_currency, customer, reference_id, request_ip, user_agent, remarks, meta_data):
        """Create Khalti Transaction Log

        Args:
            app (App):App Object
            credential_type (str): which credentail to choose from if  multiple available
            environment (str): payment live or test?
            amount (float): transaction amount
            reference_id (str): unique refernce_id of transaction
            request_ip (str): ip of request creator
            user_agent (str): user agent of request creator
            remarks (str): remarks for the transaction

        Returns:
            StripeTransaction: StripeTransaction Object
        """
        return StripeTransaction.objects.create(
            app=app,
            amount=amount,
            remarks=remarks,
            status_code="01",
            customer=customer,
            meta_data=meta_data,
            user_agent=user_agent,
            request_ip=request_ip,
            currency=charge_currency,
            reference_id=reference_id,
            transaction_date=datetime.now(),
            credential_type=credential_type.upper(),
            transaction_status=TransactionStatus.INITIATED,
            customer_name=dict_get_value("name", meta_data),
            customer_phone=dict_get_value("phone", meta_data),
            customer_email=dict_get_value("email", meta_data),
            is_test=True if environment.upper() == "TEST" else False
        )

    def create_charge(self, amount, currency, customer, email, name, token, credential):
        """Create Stripe Charge

        Args:
            amount (float): Transaction Amount
            currency (str): Currency Symbol
            credential_type (str): Type Of Credential
            environment (str): is TEST or LIVE?
            customer (str): Stripe Customer ID
            email (str): Payment Initiator Email
            name (str): Payment Initiator Name
            token (str): Stripe Sdk Generated Token
            credential (StripeCredential): Stripe Credential Object
        """
        stripe.api_key = credential.secret_key
        if not customer:
            print('**********************************')
            customer = self.create_stripe_customer(stripe, email, name, token)
            print(customer)

        try:
            return stripe.Charge.create(
                amount=amount,
                currency=currency,
                customer=customer)

        except stripe.error.CardError as e:
            return self.setError("A payment error occurred: {}".format(e.user_message), 422)
        except stripe.error.InvalidRequestError:
            return self.setError("An invalid request occurred.", 422)
        except Exception as e:
            return self.setError("Something went wrong", 500)

    def create_stripe_customer(self, stripe, email, name, token):
        """Create Stripe Customer

        Args:
            stripe (stripe): Stripe object
            email (stripe): Customer email
            name (stripe): Customer name
            token (stripe): Stripe Token
        """
        try:
            return stripe.Customer.create(
                name=name,
                email=email,
                source=token,
                description=email + " " + name,
            )
        except stripe.error.CardError as e:
            return self.setError("A payment error occurred: {}".format(e.user_message), 422)
        except stripe.error.InvalidRequestError:
            return self.setError("An invalid request occurred.", 422)
        except Exception as e:
            return self.setError("Something went wrong", 500)

    @classmethod
    def update_transaction_log(cls, log, charge, error="") -> None:
        """Update Transaction Log

        Args:
            log (StripeTransaction): Stripe Transaction Object
            charge (dict): Stripe Charge Response
        """
        if not charge:
            log.message = error
            log.transaction_status = TransactionStatus.FAILED

        else:
            log.message = charge.status
            log.status_code = "00" if charge.status == "succeeded" else "01"
            log.transaction_status = TransactionStatus.SUCCESS if charge.status == "succeeded" else TransactionStatus.ERROR

        log.save()
