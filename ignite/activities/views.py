from django.http import HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect
                             )
from .models import Activity, ActivityScore
from .forms import ActivityForm
from start_page.views import get_temperature
from accounts.views import increment_streaks, getListFriends
from json import dumps

def create_activity(request):
    context = {}
    form = ActivityForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, 'activities/create_activity.html', context)


def get_all_activities(request):
    context ={}
    context["dataset"] = Activity.objects.all()
         
    return render(request, "activities/get_all_activities.html", context)


def get_by_id(request, id):
    context ={}
    context["data"] = Activity.objects.get(id = id)
    context["lat"] = 77.4067
    a = context["data"]
    print(a.id, a.name, a.description, a.location)
    return render(request, "activities/get_by_id.html", context)


def delete_activity(request, id):

    context ={}
 
    obj = get_object_or_404(Activity, id = id)
 
 
    if request.method =="POST":
        obj.delete()
        return HttpResponse("Ok")
 
    return render(request, "activities/delete_activity.html", context)


def update_activity(request, id):
    context ={}
 
    obj = get_object_or_404(Activity, id = id)
 
    # pass the object as instance in form
    form = ActivityForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "activities/update_activity.html", context)

def ordActivities(socialScore, physicalScore, moneyScore, weather):
    """
    socialScore, physicalScore, moneyScore: quiz responses
    """
    distancesList = []
    for elem in Activity.objects.all():   #for each activity
        activScores = ActivityScore.objects.filter(activity_id = elem.id)  #for each score of one activity
        dist = 0
        for actscore in activScores:   #we calculate the distance: 
                                       #dist = |activitySocialScore-personSocialScore|+
                                       # +|activityPhysicalScore-personPhysicalScore|+|activityMoneyScore-personMoneyScore|
            if actscore.type == "social":
                dist += abs(socialScore - actscore.score )
            elif actscore.type == "physical":
                dist += abs(physicalScore - actscore.score )
            elif actscore.type == "money":
                dist += abs(moneyScore - actscore.score )
        if elem.location_type == "outdoor" and weather == "rain":   #modify distance if the weather is bad
            dist += 2
        distancesList.append((dist, elem))
    distancesList.sort()
    return distancesList

def chooseActivities(request, socialScore, physicalScore, moneyScore, weather, counter):
    """
    coutner: the number of "regresh page"s
    """
    counter = int(counter)
    socialScore = int(socialScore)
    physicalScore = int(physicalScore)
    moneyScore = int(moneyScore)

    listActivity = ordActivities(socialScore, physicalScore, moneyScore, weather) 
    if counter > len(listActivity) - 1:
        counter = 0
    your_activity = listActivity[counter][1]
    if your_activity.location_type == "indoor":
        your_activity.lat = 44.441503
        your_activity.lon = 26.016553
    counter += 1
    context = {"counter":counter, 
               "activity": your_activity}

    return render(request, "global/your_activity.html", context)


def explore(request):
    print(request.user.lat)
    print(request.user.lon)
    context = {"lat":request.user.lat, "lon": request.user.lon, "user":request.user}
    # friends = getListFriends(request)
    # send_friends(request)
    data_json = send_friends(request)
    context["friends"] = data_json
    # increment_streaks(request)
    return render(request, "global/explorer.html", context)


def start_activity(request, lat, lon):
    context = {"lat":lat, "lon":lon, "user":request.user}
    friends = getListFriends(request)
    # send_friends(request)
    data_json = send_friends(request)
    context["friends"] = data_json
    increment_streaks(request)
    return render(request, "global/explorer.html", context)

def send_friends(request):
    friends = getListFriends(request)
    package = {}
    for i in range(len(friends)):
        package[i] = [friends[i].last_name, friends[i].first_name, str(friends[i].lat), str(friends[i].lon)]

    return dumps(package)