from django.urls import path

from stripe_card.api.views.payment_views import PaymentView


urlpatterns = [
    path("payment", PaymentView.as_view(),
         name='make_stripe_payment'),
]
