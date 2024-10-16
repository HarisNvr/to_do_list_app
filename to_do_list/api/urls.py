from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ToDoViewSet

router = DefaultRouter()
router.register(r'tasks', ToDoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
