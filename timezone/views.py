
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TimezoneSerializer
from .models import Timezone

from django.utils import timezone
timezone.now()

class TimezoneAPIView(APIView):
    def get(self, request):
        serializer = TimezoneSerializer(Timezone.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        Timezone.objects.create()
        return Response(status=201)

