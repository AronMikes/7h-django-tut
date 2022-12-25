from django.forms import ModelForm

from .models import Room, Message, Region

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']

class RegionForm(ModelForm):
    class Meta:
        model=Region
        fields = ['country', 'name']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']