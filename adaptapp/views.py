from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from adaptapp.models import *
from adaptapp.serializer import BaseAdaptSerializer


class UserApiViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BaseAdaptSerializer
