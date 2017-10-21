from django.contrib.auth.models import User
from django.db import transaction
from .models import (
    Information
)
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class InformationSerializer(serializers.ModelSerializer):
    # info = serializers.ReadOnlyField()

    class Meta:
        model = Information
        extra_kwargs = {
            'email': {
                'validators': [
                    UniqueValidator(
                        queryset=Information.objects.all(),
                        message='True')
                ],
            }
        }

        fields = [
            'alias'
        ]


class InformationGetterSerializer(serializers.ModelSerializer): #as UserSerializer
    profile = InformationSerializer()

    class Meta:
        model = User
        extra_kwargs = {
            'email': {
                'required': True,
                'validators': [UniqueValidator(queryset=User.objects.all())]
            },
            'username': {
                'required': True,
            },
            'password': {
                'required': True,
            },
            'profile': {
                 'required': False,
            }
        }
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'profile',
        ]

    @transaction.atomic
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        Information.objects.filter(id=instance.profile.id).update(**profile_data)

        return instance


class SignupSerializer(serializers.ModelSerializer):
    profile = InformationSerializer()

    class Meta:
        model = User
        extra_kwargs = {
            'email': {'required': True, 'validators': [
                UniqueValidator(queryset=User.objects.all(), message='Email already exists.')
            ]},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True},
        }
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'password',
            'profile',
        ]

    @transaction.atomic
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user_id = self.context.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            User.objects.filter(id=user.id).update(**validated_data)
            Information.objects.filter(id=user.profile.id).update(**profile_data)
            user.refresh_from_db()
        except User.DoesNotExist:
            user = User(username=validated_data['email'], **validated_data)
            user.save()
            Information.objects.create(user=user, **profile_data)

        user.set_password(validated_data['password'])
        user.save()
        return user
