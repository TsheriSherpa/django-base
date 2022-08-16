from rest_framework import serializers


class AppAccessTokenSerializer(serializers.Serializer):
    secret_key = serializers.CharField(max_length=255)
    refresh_key = serializers.CharField(max_length=255)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
