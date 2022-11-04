from rest_framework import serializers

import pytz

class TimezoneSerializer(serializers.Serializer):
    FORMAT = "%Y-%m-%d %H:%M:%S"
    DB_Datetime = serializers.DateTimeField(format=FORMAT, source="datetime")
    TO_KST = serializers.SerializerMethodField()
    TO_UTC = serializers.SerializerMethodField()
    Real = serializers.SerializerMethodField()

    def get_TO_UTC(self, obj):
        return obj.datetime.astimezone(pytz.UTC).strftime(self.FORMAT)
    
    def get_TO_KST(self, obj):
        return obj.datetime.astimezone(pytz.timezone("Asia/Seoul")).strftime(self.FORMAT)

    def get_Real(self, obj):
        date = obj.datetime.replace(tzinfo=pytz.UTC)
        return  date.astimezone(pytz.timezone("Asia/Seoul")).strftime(self.FORMAT)
    