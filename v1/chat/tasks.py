from celery import task
from celery.utils.log import get_task_logger

from v1.chat.models import Chat

logger = get_task_logger(__name__)


@task(name="save_message_task")
def save_message_task(message):
    """
    Save new message
    """
    chat = Chat.objects.create(message=message)
    return chat
