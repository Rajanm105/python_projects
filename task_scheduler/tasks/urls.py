from django.urls import path
from .views import schedule_task

urlpatterns = [
    path('schedule-task/', schedule_task, name='schedule-task'),
]