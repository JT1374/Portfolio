# Imports.
from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


# Urls for main.
urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
