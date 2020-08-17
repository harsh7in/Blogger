from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.exceptions import ValidationError


UserModel = get_user_model()

# Reference - https://rahmanfadhil.com/django-login-with-email/

# Userlogin by email or username
class EmailBackend(ModelBackend):
    error_messages = {
        'invalid_login': (
            "Please enter a correct email/username and password."
        ),
        'invalid_password': (
            "Please enter a correct password."
        )
    }
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            raise self.get_invalid_login_error()
        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            else:
                raise self.get_invalid_password()

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None

    def get_invalid_login_error(self): #For invalid email and password
        return ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
        )
    
    def get_invalid_password(self): #For invalid password only
        return ValidationError(
            self.error_messages['invalid_password'],
            code='invalid_password',
        )