from rest_framework.serializers import ModelSerializer
from .models import Ticket
from rest_framework import serializers
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class TicketSerializer(ModelSerializer):
	uzytkownik = serializers.StringRelatedField(read_only=True)
	pracownik = serializers.StringRelatedField(read_only=True)
	class Meta:
		model = Ticket
		fields = '__all__'

class GoogleSocialLoginSerializer(SocialLoginSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        refresh = RefreshToken.for_user(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data