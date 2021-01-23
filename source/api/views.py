from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views.generic import View
from webapp.models import Friend


class AddFriendView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        target_user = get_object_or_404(get_user_model(), pk=kwargs.get('pk'))
        if target_user.pk == self.request.user.pk:
            return HttpResponseForbidden()
        friend, created = Friend.objects.get_or_create(target_user=target_user, user=request.user)
        if created:
            return HttpResponse()
        else:
            return HttpResponseForbidden()


class UnFriendView(LoginRequiredMixin, View):
    def delete(self, request, *args, **kwargs):
        target_user = get_object_or_404(get_user_model(), pk=kwargs.get('pk'))
        friend = get_object_or_404(Friend, user=request.user, target_user=target_user)
        friend.delete()
        return HttpResponse()