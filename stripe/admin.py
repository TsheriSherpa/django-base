from django.contrib import admin

from stripe.models import Stripe
from stripe.models import StripeCredential

admin.site.register(Stripe)
admin.site.register(StripeCredential)
