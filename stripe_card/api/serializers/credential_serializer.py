from rest_framework import serializers


class CredentialSerializer(serializers.Serializer):
    base_url = serializers.CharField(max_length=255)
    secret_key = serializers.CharField(max_length=255)
    environment = serializers.CharField(max_length=255)
    publishable_key = serializers.CharField(max_length=255)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['type'] = 'stripe'
        return data
