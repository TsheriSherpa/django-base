from django.urls import path

from esewa.api.views.esewa_payment_views import EsewaPaymentView
from esewa.api.views.esewa_web_callback_views import EsewaWebCallback

urlpatterns = [
    path("payment", EsewaPaymentView.as_view(),
         name='esewapayment'),
    path('web/callback/<status>',EsewaWebCallback.as_view(), name="esewa_web_callback")
]
