from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Trader

@receiver(post_save, sender=User)
def create_tader(instance, created, *args, **kwargs):
    if created:
        Trader.objects.create(user=instance)

