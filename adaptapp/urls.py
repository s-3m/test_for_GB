from django.urls import path, include
from rest_framework.routers import DefaultRouter
from adaptapp.views import *

router = DefaultRouter()
router.register('users', UserApiViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
