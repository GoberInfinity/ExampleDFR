from rest_framework import serializers
from .models import User, Data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)
        read_only_fields = ('username', )


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'auth_token',)
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}


class DataSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """
        Create and return a new `Data` instance, given the validated data.
        """
        return Data.objects.create(**validated_data)

    class Meta:
        model = Data
        fields = ('transaction_id', 'transaction_date', 'transaction_amount', 'client_id', 'client_name')

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(use_url=False)
