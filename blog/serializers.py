from rest_framework import serializers

class Years(serializers.Serializer):
  years=serializers.CharField()