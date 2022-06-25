from django.shortcuts import render

from Chat.models import Friend, Profile
from .forms import ChatMessageForm

# Create your views here.

def home(request):
    user = request.user.profile
    friends = user.friends.all()
    context = {
        "user":user,
        "friends":friends,
    }
    return render(request, 'home.html', context)


def detail(request, pk):
    friend = Friend.objects.get(id=pk)
    chatform = ChatMessageForm()
    context = {
        "friend":friend,
        "chatform":chatform,
    }
    return render(request, "detail.html", context)