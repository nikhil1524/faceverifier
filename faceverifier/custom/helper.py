from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


# def user_directory_path(userId, clientId):
#     return '{0}/{1}/{2}'.format(userId, clientId, clientId+'.jpg')


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


