from datetime import timedelta

from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TimezoneSerializer
from .models import Timezone

class TimezoneAPIView(APIView):
    def get(self, request):
        serializer = TimezoneSerializer(Timezone.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        Timezone.objects.create()
        return Response(status=201)

    def put(self, request):
        Timezone.objects.all().update(datetime=F("datetime") + timedelta(hours=9))
        return Response(status=200)