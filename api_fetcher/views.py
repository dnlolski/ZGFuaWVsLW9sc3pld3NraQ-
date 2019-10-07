from django_celery_beat.models import PeriodicTask
from django_celery_beat.models import IntervalSchedule
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Item
from .models import History
from .serializers import ItemSerializer
from .serializers import HistorySerializer
from .tasks import save_data_from_url


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        url = request.data['url']
        interval = request.data['interval']

        item = Item(url=url, interval=interval)
        item.save()
        item_id = item.id

        save_data_from_url.delay(url, item_id)

        schedule = IntervalSchedule.objects.create(every=f"{request.data['interval']}", period='seconds')
        task = PeriodicTask.objects.create(name=f'save_data_from_url_{item_id}',
                                           task='api_fetcher.tasks.save_data_from_url',
                                           interval=schedule,
                                           args='["{}","{}"]'.format(url, item_id))
        task.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class HistoryViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerializer

    def get_queryset(self):
        queryset = History.objects.filter(item_id=self.kwargs['item_id'])
        return queryset
