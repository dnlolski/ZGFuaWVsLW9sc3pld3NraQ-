from rest_framework import viewsets

from .serializers import ItemSerializer
from .serializers import HistorySerializer
from .models import Item
from .models import History


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    # queryset = History.objects.all()
    serializer_class = HistorySerializer

    def get_queryset(self):
        queryset = History.objects.filter(item_id=self.kwargs['item_id'])
        return queryset
