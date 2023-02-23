from .models import AoK
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class AoKSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model to serialize
        model = AoK
        # The fields to serialize
        fields = ['id', 'actor', 'recipient', 'act']
