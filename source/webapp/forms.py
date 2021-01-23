from django import forms
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from webapp.models import Message


class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        receiver_pk = kwargs.pop('receiver_pk')
        sender_pk = kwargs.pop('sender_pk')
        self.sender = get_user_model().objects.get(pk=sender_pk)
        self.receiver = get_object_or_404(get_user_model(), pk=receiver_pk)
        super(MessageForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Message
        fields = ['text']

    def clean(self):
        cleaned_data = super(MessageForm, self).clean()
        if self.sender == self.receiver:
            raise forms.ValidationError('You cannot send a message to yourself')
        return cleaned_data
