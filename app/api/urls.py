from django.urls import path
from app.api.views.app_authenticate_views import AppAuthenticateView
from app.api.views.app_credential_views import AppCredentialView


urlpatterns = [
    path("credentials", AppCredentialView.as_view(),
         name='get_payment_credentials'),
    path("authenticate", AppAuthenticateView.as_view(), name="authenticate_app"),
]
