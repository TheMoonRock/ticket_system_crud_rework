from django.urls import path
from . import views

app_name = 'equipment_manager'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]
