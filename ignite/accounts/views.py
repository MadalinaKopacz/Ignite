from multiprocessing import context
import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import FriendRequests, addFriend, userCreate, LoginForm, UpdateUserForm, ChangePasswordForm
from .models import Friend_Request, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
import requests

from django.contrib.gis.geoip2 import GeoIP2

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def update_location(request, user):
    key = "9fa76c16db4ea6572cdc950e6ec3ed42"
    current_user = get_object_or_404(User, username = user.username)
    ip = '86.121.188.6' #get_client_ip(request)
    
    g = GeoIP2()
    if ip:
        city = g.city(ip)['city']
    else:
        city = 'Bucharest' 

    url1 = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={key}"

    r1 = requests.get(url1).json()
    lon = r1[0]["lon"]
    lat = r1[0]["lat"]

    current_user.lon = lon
    current_user.lat = lat
    current_user.save()

    return 0

def increment_streaks(request):
    current_user = get_object_or_404(User, username = request.user.username)
    current_user.streaks += 1
    current_user.save()
    return 0


def login_view(request):
    if not request.user.is_anonymous: # cnv deja conectat acceseaza
        return HttpResponseRedirect('/start_page/get/')

    context = {}
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                update_location(request, user)
                login(request=request, user=user)
                return HttpResponseRedirect('/start_page/get/')
    
    context['form'] = form
    return render(request, "accounts/login.html", context)


def createView(request):
    if not request.user.is_anonymous: # cnv deja conectat acceseaza
        return HttpResponseRedirect('/start_page/get/')
    context = {}
    form = userCreate(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/login")

    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, "accounts/create.html", context)


def detailView(request, username):
    context = {}
    context["data"] = User.objects.get(username = username)

    return render(request, 'accounts/profile.html', context)

@login_required
def updateView(request):
    context = {}

    object = get_object_or_404(User, username = request.user.username)

    form = UpdateUserForm(request.POST or None, instance = object)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../profile/")
    
    context["form"] = form
    return render(request, "accounts/update.html", context)

@login_required
def changePasswordView(request):
    context = {}

    form = PasswordChangeForm(user=request.user, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'accounts/profile.html', context)

        else:
            context['error'] = "Passwords don't match."
    
    context["form"] = form
    return render(request, "accounts/changepassword.html", context)

def deleteView(request, username):
    context = {}
    object = get_object_or_404(User, username = username)

    if request.method == "POST":
        object.delete()
        return HttpResponseRedirect("/")
    
    return render(request, "accounts/deleteView.html", context)

@login_required
def getFriends(request):
    context = {}

    user = request.user
    context["data"] = user
    context["friends"] = user.friends.all()

    return render(request, 'accounts/profile.html', context)

@login_required
def profile(request):
    context = {}

    user = request.user
    context["data"] = user
    context["friends"] = user.friends.all()

    return render(request, 'accounts/profile.html', context)


@login_required
def findFriendsView(request):
    form = addFriend(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            try:
                to_user = User.objects.get(username=username)
                if request.user == to_user:
                    return render(request, "accounts/findFriends.html", {"form": form, "error":"I dont think you're so lonely you're adding yourself as a friend..."})
                elif to_user in request.user.friends.all():
                    return render(request, "accounts/findFriends.html", {"form": form, "error":"Already friends"})

                return addFriendView(request, to_user)
            except:
                return render(request, "accounts/findFriends.html", {"form": form, "error":"No user with that username"})


    return render(request, "accounts/findFriends.html", {"form": form})

@login_required
def addFriendView(request, to_user):
    from_user = request.user

    form = addFriend()

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../profile/")

    if to_user == None:
        return render(request, "accounts/findFriends.html", {"form": form, "error":"Invalid"})
    
    friend_req, created = Friend_Request.objects.get_or_create(from_user=from_user, 
    to_user = to_user)

    if created:
        return render(request, "accounts/findFriends.html", {"form": form, "error":"Request sent."})
    else:
        return render(request, "accounts/findFriends.html", {"form": form, "error":"A request already exists."})
    
@login_required
def seeFriendRequests(request):
    form = FriendRequests(user=request.user.username)

    if request.method == "POST":
        id = request.POST['requests']
        return render(request, 'accounts/seeRequests.html', {'form':form, 'error': acceptFriendView(request, id)})

    return render(request, 'accounts/seeRequests.html', {'form':form})

@login_required
def acceptFriendView(request, requestID):
    friend_req = Friend_Request.objects.get(id=requestID)
    if friend_req.to_user == request.user:
        friend_req.to_user.friends.add(friend_req.from_user)
        friend_req.from_user.friends.add(friend_req.to_user)
        friend_req.delete()
        return "Request accepted"
    else:
        return "Request denied"

@login_required
def logout_view(request):
    logout(request)
    # print("should be logged out")
    # Redirect to a success page.
    return HttpResponseRedirect("../../")

def getFriends(request):
    context = {}

    user = request.user
    context["data"] = user
    context["friends"] = user.friends.all()

    return context