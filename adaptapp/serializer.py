from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth.models import User
from adaptapp.models import *


class BaseAdaptSerializer(ModelSerializer):
    full_name = CharField(source='get_full_name')

    class Meta:
        model = User
        fields = ('full_name', 'username', 'last_login',)

#--------------------------------- Сериализаторы для пользователя --------------------------
