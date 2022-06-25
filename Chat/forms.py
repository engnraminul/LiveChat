from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import ChatMessage

class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms", "rows":2, "placeholder":"Type Message"}))
    class Meta:
        model = ChatMessage
        fields = ["body",]