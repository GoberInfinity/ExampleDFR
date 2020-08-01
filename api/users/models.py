import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Data(models.Model):
    # UUID is made of up of hex digits (4 chars each) along with 4 “-” symbols which make its length equal to 36 characters.
    transaction_id = models.CharField(max_length=40)
    # A DateField¶ can fit better but we need to be sure to parse the data correctly
    transaction_date = models.CharField(max_length=10)
    # Sample data doesn't show negative examples, if needed change the field to: IntegerField
    transaction_amount = models.PositiveIntegerField()
    # We will never have negative client_ids
    client_id = models.PositiveIntegerField()
    # We can use the max value in case of a very large name
    client_name = models.CharField(max_length=100)
