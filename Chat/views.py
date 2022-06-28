from django.shortcuts import redirect, render

from Chat.models import ChatMessage, Friend, Profile
from .forms import ChatMessageForm
from django.http import JsonResponse
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
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.profile
    profile = Profile.objects.get(id=friend.profile.id)
    chats = ChatMessage.objects.all()
    rec_chats = ChatMessage.objects.filter(msg_sender=profile, msg_receiver=user, seen=False)
    rec_chats.update(seen=True)
    form = ChatMessageForm()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = profile
            chat_message.save()
            return redirect("detail", pk=friend.profile.id)
    context = {
        "friend":friend,
        "chatform":form,
        "user":user,
        "profile":profile,
        "chats":chats,
    }
    return render(request, "detail.html", context)


def SendMessages(request, pk):
    return JsonResponse("Fine", safe=False)
