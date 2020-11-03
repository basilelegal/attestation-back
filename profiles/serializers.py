from django.db import transaction
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password',
        ]

    @staticmethod
    def validate_username(value):
        """
        Make sure that no user with this natural key exists.
        This can be used to make usernames case-insensitive, e.g.,
        disallow the registration of two different usernames which
        are equal but with different case.
        """
        try:
            get_user_model().objects.get_by_natural_key(value)
        except get_user_model().DoesNotExist:
            return value
        else:
            raise ValidationError('already exists')

    @staticmethod
    def validate_password(value):
        if len(value) < 6:
            raise ValidationError('password too short')
        return value

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop('password')

        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()

        return instance
