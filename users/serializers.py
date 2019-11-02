# api rest
from rest_framework import serializers
from users.models import CustomUser, Assistance

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = '__all__'

class AssistanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Assistance
		fields = '__all__'
