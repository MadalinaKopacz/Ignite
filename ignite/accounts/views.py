from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import FriendRequests, addFriend, userCreate
from .models import Friend_Request, User
from django.contrib.auth.decorators import login_required

# Create your views here.
def createView(request):
    context = {}
    form = userCreate(request.POST or None, request.FILES or None)

    if request.method == "POST":
        return profile(request)

    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, "accounts/create.html", context)


def detailView(request, username):
    context = {}
    context["data"] = User.objects.get(username = username)

    return render(request, 'accounts/detailView.html', context)


def updateView(request, username):
    context = {}

    object = get_object_or_404(User, username = username)

    form = userCreate(request.POST or None, instance = object)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../detailView/" + object.username)

    context["form"] = form
    return render(request, "accounts/update.html", context)


def deleteView(request, username):
    context = {}
    object = get_object_or_404(User, username = username)

    if request.method == "POST":
        object.delete()
        return HttpResponseRedirect("/")
    
    return render(request, "accounts/deleteView.html", context)

@login_required
def profile(request):
    context = {}

    user = request.user
    context["data"] = user
    context["friends"] = user.friends.all()

    return render(request, 'accounts/detailView.html', context)


@login_required
def findFriendsView(request):
    form = addFriend(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            to_user = User.objects.get(username=username)
            return addFriendView(request, to_user)

    return render(request, "accounts/findFriends.html", {"form": form})

@login_required
def addFriendView(request, to_user):
    from_user = request.user

    form = addFriend()

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../detailView/" + object.username)

    if to_user == None:
        return HttpResponse("Invalid")
    
    friend_req, created = Friend_Request.objects.get_or_create(from_user=from_user, 
    to_user = to_user)

    if created:
        return HttpResponse("Request sent")
    else:
        return HttpResponse("A request already exists")
    
@login_required
def seeFriendRequests(request):
    form = FriendRequests(user=request.user.username)

    if request.method == "POST":
        if form.is_valid():
            id = form.cleaned_data.get('id')
            return acceptFriendView(request, id)

    return render(request, 'accounts/seeRequests.html', {'form':form})

@login_required
def acceptFriendView(request, requestID):
    friend_req = Friend_Request.objects.get(id=requestID)

    if friend_req.to_user == request.user:
        friend_req.to_user.friends.add(friend_req.from_user)
        friend_req.from_user.friends.add(friend_req.to_user)
        friend_req.delete()
        return HttpResponse("Request accepted")
    else:
        return HttpResponse("Request denied")

