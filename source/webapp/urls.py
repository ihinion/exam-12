from django.urls import path
from .views import MessageCreateView, MessageBoxView, IncomingMessagesListView, OutcomingMessagesListView,\
    MessageDetailView

app_name = 'webapp'


urlpatterns = [
    path('accounts/<int:pk>/messages/send/', MessageCreateView.as_view(), name='message_create'),
    path('messages/', MessageBoxView.as_view(), name='message_box'),
    path('messages/inbox/', IncomingMessagesListView.as_view(), name='messages_incoming'),
    path('messages/outbox/', OutcomingMessagesListView.as_view(), name='messages_outcoming'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
]
