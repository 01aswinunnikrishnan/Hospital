from rest_framework import serializers

class CredentialsSerializer(serializers.Serializer):
    token = serializers.CharField()
    refresh_token = serializers.CharField()
    token_expiry = serializers.DateTimeField()

class DoctorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
