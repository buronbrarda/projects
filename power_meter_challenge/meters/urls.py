from rest_framework import routers

from .api import MeterViewSet, MeasureViewSet

router = routers.DefaultRouter()

router.register('api/meters', MeterViewSet, 'meters')
router.register('api/measures', MeasureViewSet, 'measures')

urlpatterns = router.urls