from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Seller


def seller_profile(sender, instance, created, **kwargs):
    if created:
        #group = Group.objects.get(name='Seller')
        # instance.groups.add(group)
        Seller.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
        )


post_save.connect(seller_profile, sender=User)
