from users.models import Profile
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_no', 'institute', 'date_of_birth']


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'password',
                  'email', 'first_name', 'last_name']

    # taking from parent class
    # create method will call this
    # def perform_create(self, validated_data):
    #     with transaction.atomic():
    #         user = User.objects.create_user(**validated_data)
    #         if settings.SEND_ACTIVATION_EMAIL:
    #             user.is_active = False
    #             user.save(update_fields=["is_active"])
    #     return user


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'first_name']
