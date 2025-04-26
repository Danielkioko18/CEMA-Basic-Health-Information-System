from rest_framework import serializers
from .models import Client, HealthProgram

# Serializer to convert HealthProgram model instances to JSON format
class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram # Specify the model to serialize
        fields = ['id', 'name', 'description'] # Fields to include in the serialized output

# Serializer to convert Client model instances to JSON format,
# including nested serialization of the client's enrolled health programs
class ClientProfileSerializer(serializers.ModelSerializer):
    # Serialize the enrolled_programs field
    enrolled_programs = HealthProgramSerializer(many=True)

    class Meta:
        model = Client # Specify the model to serialize
        fields = ['id', 'first_name', 'last_name', 'contact_number', 'date_of_birth', 'gender', 'enrolled_programs']
         # List of fields to include in the serialized output