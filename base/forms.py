from django.forms import ModelForm

from .models import Room, Message

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']