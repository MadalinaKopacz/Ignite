from multiprocessing import context
import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import FriendRequestsForm, AddFriendForm, UserCreateForm, LoginForm, UpdateUserForm, ChangePasswordForm
from .models import Friend_Request, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
import requests
from django.contrib.gis.geoip2 import GeoIP2


def get_client_ip(request):
    """
    method that retrievs the ip adress of the user that makes the request
        args: request
        returns: ip address    
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def update_location(request, user):
    """
        method that update the current location of the user that makes the request
        Args: request, user
        Returns: 0 
    """ 

    key = "9fa76c16db4ea6572cdc950e6ec3ed42"
    current_user = get_object_or_404(User, username = user.username)
    ip = '86.121.188.6' # get_client_ip(request)
    # because server runs on local host, can't extract the location from ip
    
    g = GeoIP2()
    if ip:
        city = g.city(ip)['city']
    else:
        city = 'Bucharest' 

    url1 = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={key}" # connection to api

    r1 = requests.get(url1).json()
    lon = r1[0]["lon"]
    lat = r1[0]["lat"]

    current_user.lon = lon
    current_user.lat = lat
    current_user.save()

    return 0


def increment_streaks(request):
    """
    method that increments the streaks of a user
        Args: request
        Returns: 0
    """

    current_user = get_object_or_404(User, username = request.user.username)
    current_user.streaks += 1
    current_user.save()
    return 0


@login_required
def get_streaks(request):
    """
    method that returns the streak number of the session/request user
    """
    return get_object_or_404(User, username = request.user.username).streaks


def getListFriends(request):
    """
    method that returns a list of the request user's friends
    """
    return request.user.friends.all()


#Views
def login_view(request):
    """
    method for the user login
        Args: request
        Returns: renders login page 
    """
    if not request.user.is_anonymous: # Somebody already connected tries to access
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


def create_view(request):
    """
    method for user creation
        Args: request
        Returns: renders the user creation form
    """
    
    if not request.user.is_anonymous: # Somebody already connected tries to access
        return HttpResponseRedirect('/start_page/get/')
    context = {}
    form = UserCreateForm(request.POST or None, request.FILES or None)

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
def update_view(request):
    """
    method that updates the details of a user
        Args: requesst
        Returns: the update page
    """

    context = {}

    object = get_object_or_404(User, username = request.user.username)

    form = UpdateUserForm(request.POST or None, instance = object)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../profile/")
    
    context["form"] = form
    return render(request, "accounts/update.html", context)


@login_required
def change_password_view(request):
    """
    request for changing the user's password
        Args: request
        Returns: the HTML changepassword page
    """

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


def delete_view(request, username):
    """
    method that deletes a user from the database
        Args: request, username
        Returns: the HTML page for deleting the user
    """

    context = {}
    object = get_object_or_404(User, username = username)

    if request.method == "POST":
        object.delete()
        return HttpResponseRedirect("/")
    
    return render(request, "accounts/deleteView.html", context)


@login_required
def profile(request):
    """
    method that returns the profile of a user and the list of friends
        Args: request
        Returns: the profile page
    """
    context = {}

    user = request.user
    context["data"] = user
    context["friends"] = user.friends.all()

    return render(request, 'accounts/profile.html', context)


@login_required
def find_friends_view(request):
    """
    method that finds the user for the friend request
        Args: request
        Returns: 1 HTML page with the appropiate response 
    """
    form = AddFriendForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            try:
                to_user = User.objects.get(username=username)
                if request.user == to_user:
                    return render(request, "accounts/findFriends.html", {"form": form, "error":"I dont think you're so lonely you're adding yourself as a friend..."})
                elif to_user in request.user.friends.all():
                    return render(request, "accounts/findFriends.html", {"form": form, "error":"Already friends"})

                return add_friend_view(request, to_user)
            except:
                return render(request, "accounts/findFriends.html", {"form": form, "error":"No user with that username"})


    return render(request, "accounts/findFriends.html", {"form": form})


@login_required
def add_friend_view(request, to_user):
    """
    method that adds the new friend to the current user's friendlist
        Args: request, to_user (username of the new friend)
        Returns: HTML page with appropiate response
    """
    from_user = request.user

    form = AddFriendForm()

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
def see_friend_requests_view(request):
    """
    method that returns all the pending friend requests
        Args: request
        Returns: HTML page
    """
    form = FriendRequestsForm(user=request.user.username)

    if request.method == "POST":
        id = request.POST['requests']
        return render(request, 'accounts/seeRequests.html', {'form':form, 'error': accept_friend_view(request, id)})

    return render(request, 'accounts/seeRequests.html', {'form':form})


@login_required
def accept_friend_view(request, requestID):
    """
    method that accepts a pending friend request
        Args: request, requestID (id of the friend request)
        Returns: a message according to the user's action (accept/deny)
    """
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
    """
    method that logs out the current logged in user
        Args: request
        Returns: redirects to the login/register page
    """
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("../../")
