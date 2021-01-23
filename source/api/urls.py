from django.urls import path
from .views import AddFriendView, UnFriendView

app_name = 'api'


urlpatterns = [
    path('user/<int:pk>/addfriend/', AddFriendView.as_view(), name='addfriend'),
    path('user/<int:pk>/unfriend/', UnFriendView.as_view(), name='unfriend'),
]