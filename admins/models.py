from django.db import models

# Create your models here.


class Information(models.Model):
    alias = models.CharField(max_length=30, null=True, blank=True)
    creation_date = models.DateTimeField('date created', auto_now_add=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    repassword = models.CharField(max_length=30, null=True, blank=True)
    # image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
