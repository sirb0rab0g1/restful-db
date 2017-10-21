from django.contrib import admin

# Register your models here.
from .models import (
    Messaging
)


@admin.register(Messaging)
class InformationAdmin(admin.ModelAdmin):
    list_display = [
        'user_id', 'msg', 'receiver_id'
    ]
