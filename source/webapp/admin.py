from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from webapp.models import Friend, Message


admin.site.register(Friend)
admin.site.register(Message)
