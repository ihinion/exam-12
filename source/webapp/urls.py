from django.urls import path
from .views import MessageCreateView

app_name = 'webapp'


urlpatterns = [
    path('accounts/<int:pk>/messages/send/', MessageCreateView.as_view(), name='message_create'),
]
