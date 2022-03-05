from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Profile
from rest_framework.authtoken.models import Token


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=20)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')

        return data


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user', )


class TokenSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        user_id = serializers.IntegerField(source='id')

        class Meta:
            model = get_user_model()
            fields = ('user_id', 'username', 'nickname', )

    user = UserSerializer(read_only=True)

    class Meta:
        model = Token
        fields = ('key', 'user',)