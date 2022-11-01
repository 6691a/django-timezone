from rest_framework import serializers

from django.utils import timezone


timezone.now()

class TimezoneSerializer(serializers.Serializer):
    datetime = serializers.DateTimeField()
    