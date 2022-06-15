from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .models import Activity, ActivityScore
from .forms import ActivityForm
from accounts.views import increment_streaks, getListFriends
from json import dumps


def create_activity(request):
    """
    method for activity creation
        Args: request
        Returns: html page with a creation form
    """
    context = {}
    form = ActivityForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, 'activities/create_activity.html', context)


def get_all_activities(request):
    """
    method that queries the database and provides all the registered activities
        Args: request
        Returns: html page that displays all activities
    """
    context ={}
    context["dataset"] = Activity.objects.all()
         
    return render(request, "activities/get_all_activities.html", context)


def get_by_id(request, id):
    """"
    method that retrievies the activity with a specified id
        Args: request
        Returns: HTML page of the activity
    """
    context ={}

    context["data"] = Activity.objects.get(id = id)
    context["lat"] = 77.4067

    return render(request, "activities/get_by_id.html", context)


def delete_activity(request, id):
    """
    method that deletes an activity with a specified id
        Args: request, id (of the activity that should be deleted)
        Returns: HTML page or HTTPResponse 
    """
    context ={}
    obj = get_object_or_404(Activity, id = id)
 
    if request.method =="POST":
        obj.delete()
        return HttpResponse("Ok")
 
    return render(request, "activities/delete_activity.html", context)


def update_activity(request, id):
    """
    method that updates the details of an activity
        Args: request, id (of the activity)
        Returns: HTML page with the update form
    """
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
    method that sorts the activities based of the scores, weather and distance
        Args: socialScore, pyhsicalScore, moneyScore (numbers from 1 to 10)
              weather (string that describes the current weather)
        Returns: list of sorted activities
    """
    distancesList = []

    for elem in Activity.objects.all():   #for each activity
        activScores = ActivityScore.objects.filter(activity_id = elem.id)  #for each score of one activity
        dist = 0

        for actscore in activScores:  
            #we calculate the distance: 
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
    method that selects the best fitting activity based on the quizz
        Args: request, scores, weather
              counter -> number of refreshes of the page
        Returns: the HTML page of the activity
    """
    counter = int(counter)
    socialScore = int(socialScore)
    physicalScore = int(physicalScore)
    moneyScore = int(moneyScore)

    listActivity = ordActivities(socialScore, physicalScore, moneyScore, weather) 
    
    if counter > len(listActivity) - 1:
        counter = 0
    your_activity = listActivity[counter][1]

    if your_activity.location_type == "indoor" or your_activity.location_type == "any":
        your_activity.lat = 44.441503
        your_activity.lon = 26.016553
        
    counter += 1
    context = {"counter":counter, 
               "activity": your_activity,
               "socialscore":socialScore,
               "physicalscore":physicalScore,
               "moneyscore":moneyScore,
               "weather":weather
               }

    return render(request, "global/your_activity.html", context)


def explore(request):
    """
    method for getting the data needed to compute the explore page
    """
    context = {"lat": request.user.lat, "lon": request.user.lon, "user":request.user}
    data_json = send_friends(request)
    context["friends"] = data_json
    return render(request, "global/explorer.html", context)


def start_activity(request, lat, lon):
    """
    method for accepting the activity
        Args: request,
              lat, lon -> location of the activity
        Returns: explorer page
    """

    context = {"lat":lat, "lon":lon, "user":request.user}
    
    data_json = send_friends(request)
    context["friends"] = data_json

    increment_streaks(request)
    return render(request, "global/explorer.html", context)


def send_friends(request):
    """
    method to transform a list to a dictionary, to be sent using json to javascript
    """
    friends = getListFriends(request)
    package = {}
    for i in range(len(friends)):
        package[i] = [friends[i].last_name, friends[i].first_name, str(friends[i].lat), str(friends[i].lon)]

    return dumps(package)