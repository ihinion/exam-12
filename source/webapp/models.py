from django.contrib.auth import get_user_model
from django.db import models


class Friend(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name='User', related_name='friends',
                             on_delete=models.CASCADE)
    target_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                    verbose_name='Friend')


class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), verbose_name='Sender', related_name='messages',
                               on_delete=models.CASCADE)
    receiver = models.ForeignKey(get_user_model(), verbose_name='Receiver', on_delete=models.CASCADE)
    text = models.TextField(max_length=500, verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')