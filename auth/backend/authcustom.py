from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class SettingsBackend(BaseBackend):
    """
    Usage of custom authentication.

    """

    def authenticate(self, request, username=None, password=None):


            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                resp = request('localhost:8081/login');
                if resp.status(400):

                    user = User(username=resp.username)
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                    return user
        # return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None