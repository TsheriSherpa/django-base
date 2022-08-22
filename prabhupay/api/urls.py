from django.urls import path
from prabhupay.api.views import (
    WebPaymentView,
    WebVerifyView,
    MobileVerifyView
)

urlpatterns = [
    path("payment/web", WebPaymentView.as_view()),
    path("payment/web/verify", WebVerifyView.as_view()),
    path("payment/mobile/verify", MobileVerifyView.as_view())
]
