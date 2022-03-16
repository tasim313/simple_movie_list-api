from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('movie', MovieViewSet)
router.register('action', ActionViewSet)
router.register('comedy', ComedyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]