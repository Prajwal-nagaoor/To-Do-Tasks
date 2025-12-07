from rest_framework import serializers
from django.contrib.auth.models import User

class auth_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)   # 🔥 IMPORTANT
        user.save()
        return user
    
class login_serializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
