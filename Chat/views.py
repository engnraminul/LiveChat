from django.shortcuts import render

from Chat.models import Friend, Profile

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
    context = {
        "friend":friend,
    }
    return render(request, "detail.html", context)