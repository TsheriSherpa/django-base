from django.contrib.auth import authenticate
from app.models import App

from rest_framework import exceptions
from rest_framework import authentication


class IsAuthenticatedApp(authentication.BaseAuthentication):
    """Authenticate App Using Username And Password From Header

    Args:
        authentication (BaseAuthentication): Extending Base Class

    Raises:
        exceptions.AuthenticationFailed: Throws Username and Password Authentication Failure

    Returns:
        App: Request Authenticated App
    """

    def authenticate(self, request):
        auth = self.get_authorization_header(request)
        username = auth.get("username")
        password = auth.get("password")

        app = App.objects.first()
        if not app:
            raise exceptions.AuthenticationFailed(('Authentication Failure'))

        request.app = app
        return (app, None)

    @staticmethod
    def get_authorization_header(request):
        """
        Return request's 'Authorization:' header, as a bytestring.
        """

        username = request.headers.get("username")
        password = request.headers.get("password")

        return {'username': username, 'password': password}
