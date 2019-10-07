from rest_framework import serializers

from .models import Item
from .models import History


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'url', 'interval')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('response', 'duration', 'created_at')
