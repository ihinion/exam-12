from django.urls import path
from .views import MessageCreateView, MessageBoxView, IncomingMessagesListView

app_name = 'webapp'


urlpatterns = [
    path('accounts/<int:pk>/messages/send/', MessageCreateView.as_view(), name='message_create'),
    path('messages/', MessageBoxView.as_view(), name='message_box'),
    path('messages/inbox/', IncomingMessagesListView.as_view(), name='messages_incoming'),
]
