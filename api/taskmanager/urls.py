from django.urls import path
from .views import ListProjectsView, LoginView, RegisterUsers
from django.views.generic import TemplateView

urlpatterns = [
    path('projects/', ListProjectsView.as_view(), name="projects-all"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsers.as_view(), name="auth-register") 
]
