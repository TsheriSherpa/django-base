from django.urls import path
from imepay.api.views.imepay_payment_views import ImepayPaymentView


urlpatterns = [
    path("payment", ImepayPaymentView.as_view(),
         name='imepayment'),
   
]
