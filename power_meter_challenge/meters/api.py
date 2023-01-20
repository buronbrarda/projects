from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Sum, Avg

from .models import Meter, Measure
from .serializers import MeterSerializer, MeasureSerializer, MeterMeasuresSerializer

class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MeterSerializer

    @action(detail=True)
    def max(self,request,*args, **kwargs):
        max = self.get_object().measures.order_by('-consumption')[0]
        serializer = MeasureSerializer(max)
        return Response(serializer.data)
    
    @action(detail=True)
    def min(self,request,*args, **kwargs):
        min = self.get_object().measures.order_by('consumption')[0]
        serializer = MeasureSerializer(min)
        return Response(serializer.data)

    @action(detail=True)
    def total(self,request,*args, **kwargs):
        value = self.get_object().measures.aggregate(Sum('consumption'))["consumption__sum"]
        return Response({"value":value})
    
    @action(detail=True)
    def avg(self,request,*args, **kwargs):
        value = self.get_object().measures.aggregate(Avg('consumption'))["consumption__avg"]
        return Response({"value":value})

class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measure.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MeasureSerializer






