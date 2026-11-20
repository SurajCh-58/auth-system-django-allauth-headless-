from rest_framework import serializers
from account.models import User,Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['full_name','email']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['image']