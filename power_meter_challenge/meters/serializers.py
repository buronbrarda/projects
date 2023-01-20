from rest_framework import serializers
from .models import Meter, Measure


class MeasureSerializer(serializers.ModelSerializer):

    timestamp = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')


    class Meta:
        model = Measure
        fields = ('id','meter','timestamp','consumption')


# This is a special serializer to use when retrieving Meter(s) since we already know the Meter code.
class MeterMeasuresSerializer(serializers.ModelSerializer):

    timestamp = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Measure
        fields = ('id','timestamp','consumption')


class MeterSerializer(serializers.ModelSerializer):
    measures = MeterMeasuresSerializer(many=True)

    class Meta:
        model = Meter
        fields = ('code','name','measures')
        read_only_fields = ('measures', )