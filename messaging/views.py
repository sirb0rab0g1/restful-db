from rest_framework import (
    viewsets,
)
from .models import (
    Messaging
)
from .serializers import (
    MessagingSerializer
)
from rest_framework.permissions import AllowAny
from channels import Group
from rest_framework.generics import CreateAPIView
from django.db import transaction
# import json
from rest_framework.response import Response
from rest_framework import (
    status,
)
from rest_framework import generics
# from django.contrib.auth.signals import user_logged_in


class MessagingViewSet(viewsets.ModelViewSet):
    queryset = Messaging.objects.all()
    serializer_class = MessagingSerializer
    permission_classes = [
        AllowAny,
    ]


class PerUserMessage(generics.ListAPIView):
    serializer_class = MessagingSerializer

    def get_queryset(self):
        receiver_id = self.kwargs['receiver_id']
        return Messaging.objects.filter(receiver_id=receiver_id)



class MessageSetter(CreateAPIView):
    serializer_class = MessagingSerializer
    permission_classes = [
        AllowAny,
    ]

    @transaction.atomic
    def post(self, request, format=None):
        data = request.data.copy()
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            user = serializer.save()
            Group('wsmessaging').send({'text': 'lol'})
            return Response({
                'text': 'orayt'
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
