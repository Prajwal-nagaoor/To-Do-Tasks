from rest_framework import serializers

from .models import taskmodel

class taskserializer(serializers.ModelSerializer):
    class Meta:
        model = taskmodel
        fields = '__all__'