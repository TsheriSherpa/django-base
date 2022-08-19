from django.urls import path
from prabhupay.api.views import WebPaymentView


urlpatterns = [
    path("payment/web", WebPaymentView.as_view()),
]
