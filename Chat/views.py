from django.shortcuts import redirect, render

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


def detail(request,pk):
    friend = Friend.objects.get(id=pk)
    user = request.user.profile
    profile = Profile.objects.get(id=friend.profile.id)
    chatform = ChatMessageForm()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receciver = profile
            chat_message.save()
            return redirect("detail", pk=friend.profile.id)
    context = {
        "friend":friend,
        "chatform":chatform,
        "user":user,
        "profile":profile,
    }
    return render(request, "detail.html", context)