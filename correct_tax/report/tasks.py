import os

from celery import shared_task


@shared_task
def delete_out_file(filepath: str) -> None:
    os.remove(filepath)