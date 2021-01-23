from django.contrib.auth import get_user_model
from django.db import models


class Friend(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name='User', related_name='friends',
                             on_delete=models.CASCADE)
    target_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                    verbose_name='Friend')
