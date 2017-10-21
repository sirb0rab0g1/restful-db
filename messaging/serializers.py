from rest_framework import serializers
from .models import (
    Messaging,
)
# from rest_framework.validators import UniqueValidator


class MessagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messaging

        fields = '__all__'