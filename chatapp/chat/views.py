from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ChatRoom, Message
from .serializers import MessageSerializer

class SendMessageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, room_id):
        room = ChatRoom.objects.get(id=room_id)

        message = Message.objects.create(
            room=room,
            sender=request.user,
            content=request.data['content']
        )

        return Response(MessageSerializer(message).data)
