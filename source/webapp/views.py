from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView
from webapp.forms import MessageForm
from webapp.models import Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'messages/message_create.html'
    model = Message
    form_class = MessageForm

    def get_form_kwargs(self):
        kwargs = super(MessageCreateView, self).get_form_kwargs()
        receiver_pk = self.kwargs.get('pk')
        sender_pk = self.request.user.pk
        kwargs.update({
            'receiver_pk': receiver_pk,
            'sender_pk': sender_pk,
        })
        return kwargs

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.receiver = get_object_or_404(get_user_model(), pk=self.kwargs['pk'])
        message.save()
        return redirect('user_list')
