# serializer.py
from rest_framework import serializers

from app.models import Person


class personserializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'