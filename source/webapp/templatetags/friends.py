from django import template

from webapp.models import Friend

register = template.Library()


@register.filter
def is_friend(user_obj, user):
    friends = Friend.objects.filter(target_user=user_obj, user=user)
    if user_obj.pk != user.pk and friends.count() > 0:
        return True