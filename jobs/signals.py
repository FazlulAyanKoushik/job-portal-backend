from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import JobPost


@receiver(post_save, sender=JobPost)
def notify_job_status_update(sender, instance, created, **kwargs):
    if not created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'job_status_updates',
            {
                'type': 'job_status_update',
                'data': {
                    'id': instance.id,
                    'title': instance.title,
                    'status': instance.status,
                }
            }
        )
