from django.contrib.auth import get_user_model
from rest_framework import serializers
import djoser

User = get_user_model()



class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email',)