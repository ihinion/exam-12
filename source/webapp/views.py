from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView, ListView, DetailView
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
        return redirect('webapp:message_box')


class MessageBoxView(LoginRequiredMixin, TemplateView):
    template_name = 'messages/message_box.html'


class IncomingMessagesListView(LoginRequiredMixin, ListView):
    template_name = 'messages/message_inbox.html'
    model = Message
    context_object_name = 'messages'
    paginate_by = 5
    ordering = ['-id']

    def get_queryset(self):
        queryset = super(IncomingMessagesListView, self).get_queryset()
        queryset = queryset.filter(receiver=self.request.user)
        return queryset


class OutcomingMessagesListView(LoginRequiredMixin, ListView):
    template_name = 'messages/message_outbox.html'
    model = Message
    context_object_name = 'messages'
    paginate_by = 5
    ordering = ['-id']

    def get_queryset(self):
        queryset = super(OutcomingMessagesListView, self).get_queryset()
        queryset = queryset.filter(sender=self.request.user)
        return queryset


class MessageDetailView(LoginRequiredMixin, DetailView):
    template_name = 'messages/message_detail.html'
    model = Message