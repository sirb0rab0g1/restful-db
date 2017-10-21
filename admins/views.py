from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from admins.serializers import UserSerializer, GroupSerializer
from rest_framework.permissions import AllowAny
from .serializers import (
    InformationGetterSerializer
)


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': InformationGetterSerializer(
            user, context={'request': request}).data
    }


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        AllowAny,
    ]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
