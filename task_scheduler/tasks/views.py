from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import print_message_task

@api_view(['POST'])
def schedule_task(request):
    message = request.data.get('message', 'Hello from Celery!')
    delay = int(request.data.get('delay',5))
    print_message_task.apply_async(args=[message], countdown=delay)
    return Response({"status": "scheduled", "message": message, "delay": delay})
