
from rest_framework import viewsets
from rest_framework import permissions
from .models import Projects
from.serializers import ProjectsSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = (permissions.AllowAny,)
