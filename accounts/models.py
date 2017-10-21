from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Information(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    alias = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()
