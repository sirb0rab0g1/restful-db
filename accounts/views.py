import json

from channels import Group
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.db import transaction
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import (
    viewsets,
)
from rest_framework import (
    status,
)
from .serializers import (
    # InformationSerializer,
    InformationGetterSerializer,
    SignupSerializer
)
from whoyouproject.utils import generate_jwt_token


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': InformationGetterSerializer(
            user, context={'request': request}).data
    }


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = InformationGetterSerializer
    permission_classes = [
        AllowAny,
    ]


class SignupView(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny,
    ]

    @transaction.atomic
    def post(self, request, format=None):
        data = request.data.copy()
        user_id = data.pop('user_id', 0)
        # data['profile'] = profile_type
        serializer = self.serializer_class(data=data, context={'user_id': user_id})
        if serializer.is_valid():
            user = serializer.save()
            user_logged_in.send(sender=user.__class__, request=request, user=user)
            Group('wsregister').send({'text': json.dumps(data)})
            return Response({
                'token': generate_jwt_token(user),
                'user': InformationGetterSerializer(user).data,
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
