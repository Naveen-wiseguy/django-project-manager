from rest_framework import routers
from api.taskmanager.viewsets import ProjectViewSet

router = routers.DefaultRouter()

router.register(r'project', ProjectViewSet)
