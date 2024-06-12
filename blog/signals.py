from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
from .models import Blog 

@receiver(post_delete, sender=Blog)
def delete_thumbnail_on_post_delete(sender, instance, **kwargs):
    if instance.thumbnail:
        if default_storage.exists(instance.thumbnail.path):
            default_storage.delete(instance.thumbnail.path)
