from celery import shared_task
import time


@shared_task
def send_emails():
    for x in range(10):
        time.sleep(10)

        print(f'sendinf email {x}')