from django.urls import path
from app.api.views.app_credential_views import AppCredentialView


urlpatterns = [
    path("credentials", AppCredentialView.as_view(),
         name='get_payment_credentials'),
]
