from django.urls import path
from .views import SendMessageView

urlpatterns = [
    path('send/<int:room_id>/', SendMessageView.as_view()),
]
