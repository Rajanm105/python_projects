from celery import shared_task
import time

@shared_task
def print_message_task(message):
    print(f"[START] {message}")
    time.sleep(3)
    print(f"[DONE] {message}")
    return f"Processed: {message}"