from django.urls import path

from esewa.api.views.esewa_payment_views import EsewaPaymentView

urlpatterns = [
    path("payment", EsewaPaymentView.as_view(),
         name='esewapayment'),
]
