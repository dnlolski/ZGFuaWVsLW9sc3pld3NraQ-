from django.urls import include
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('api/fetcher', views.ItemViewSet)
router.register(r'api/fetcher/(?P<item_id>\d+)/history', views.HistoryViewSet, basename='History')


urlpatterns = [
    path('', include(router.urls)),
]
