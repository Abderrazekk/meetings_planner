from django.urls import path
from . import views

urlpatterns = [
    path('list', views.meeting_list, name='meeting_list'),
    path('new', views.new, name='new'),  # Route pour la création
    path('<int:id>', views.detail, name='detail'),
    path('<int:id>/delete', views.delete, name='delete'),
]