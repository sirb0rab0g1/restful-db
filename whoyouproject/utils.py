import os

from django.contrib.auth.signals import user_logged_in

from rest_framework_jwt.settings import api_settings


class classproperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


def upload_image_path(instance, filename):
    return os.path.join('images', instance.__class__.__name__.lower(), str(instance.id), filename)


def generate_jwt_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)


def update_last_login(request):
    user = request.user
    if user.is_authenticated():
        user_logged_in.send(sender=user.__class__, request=request, user=user)
