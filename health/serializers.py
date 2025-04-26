from rest_framework import serializers
from .models import Client, HealthProgram

class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = ['id', 'name', 'description']

class ClientProfileSerializer(serializers.ModelSerializer):
    enrolled_programs = HealthProgramSerializer(many=True)

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'contact_number', 'date_of_birth', 'gender', 'enrolled_programs']
