from django.contrib import admin

from stripe.models import StripeTransaction
from stripe.models import StripeCredential

admin.site.register(StripeTransaction)
admin.site.register(StripeCredential)
