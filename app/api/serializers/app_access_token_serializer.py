from rest_framework import serializers


class AppAccessTokenSerializer(serializers.Serializer):
    refresh_key = serializers.CharField(required=True, max_length=255)
