from django.http import HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect
                             )
from .models import Activity
from .forms import ActivityForm


def create_activity(request):
    context ={}
    form = ActivityForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, 'activities/create_activity.html', context)


def get_all_activities(request):
    context ={}
    context["dataset"] = Activity.objects.all()
         
    return render(request, "get_all_activities.html", context)


def get_by_id(request, id):
    context ={}
    context["data"] = Activity.objects.get(id = id)
        
    return render(request, "get_by_id.html", context)


def delete_activity(request, id):

    context ={}
 
    obj = get_object_or_404(Activity, id = id)
 
 
    if request.method =="POST":
        obj.delete()
        return HttpResponse("Ok")
 
    return render(request, "delete_activity.html", context)


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
 
    return render(request, "update_activity.html", context)