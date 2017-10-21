from django.db import models

# Create your models here.


class Messaging(models.Model):
    user_id = models.IntegerField(null=False, blank=False)
    receiver_id = models.IntegerField(null=False, blank=False)
    msg = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.msg
