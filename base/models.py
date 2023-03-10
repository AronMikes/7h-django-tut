from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = CountryField(blank_label='(select country)')

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete= models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    #description = models.TextField(null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):

    class Meta:
        ordering = ['-updated', '-created']
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]