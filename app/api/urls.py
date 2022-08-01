from django.urls import path
from app.api.views.app_views import AppView


urlpatterns = [
    path("/", AppView.get_credentials, name='get_payment_credentials'),
]
