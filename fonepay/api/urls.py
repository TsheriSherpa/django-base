from django.urls import path

from fonepay.api.views import PaymentView


urlpatterns = [
    path("payment", PaymentView.as_view(),
         name='initiate_fonepay_payment'),
]
