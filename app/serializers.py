from rest_framework import serializers
from .models import User, Lodge

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LodgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lodge
        fields = '__all__'
