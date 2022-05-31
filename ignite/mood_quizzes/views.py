from multiprocessing import context
from django.shortcuts import render
from .forms import QuestionCreateForm, QuestionUpdateForm, QuestionUpdateTextForm, QuestionUpdateTypeForm
from .models import Question
from django.shortcuts import get_object_or_404, HttpResponseRedirect

# Create your views here.
def createView(request):
    context = {}
    form = QuestionCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, "quizzes/createquestion.html", context)


def listView(request):
    context ={}
 
    context["dataset"] = Question.objects.all()
         
    return render(request, "quizzes/readquestion.html", context)


def questionsByType(request, type):
    context ={}
 
    context["dataset"] = Question.objects.filter(type = type)
         
    return render(request, "quizzes/readquestion.html", context)


def questionById(request, id):
    context ={}
 
    context["data"] = get_object_or_404(Question, id = id)
         
    return render(request, "quizzes/readquestion1.html", context)


def deleteQuestionById(request, id):
    context ={}
    obj = get_object_or_404(Question, id = id)
 
 
    if request.method =="POST":
        obj.delete()  #delete object
        return HttpResponseRedirect("/") #return to home page
 
    return render(request, "quizzes/deleteQId.html", context)

def deleteQuestionsByType(request, type):
    context ={}
 
 
    if request.method =="POST":
        Question.objects.filter(type = type).delete()
        return HttpResponseRedirect("/") #return to home page
 
    return render(request, "quizzes/deleteQs.html", context)

def deleteAllQuestions(request):
    context ={}

    if request.method =="POST":
        Question.objects.all().delete()
        return HttpResponseRedirect("/") #return to home page
 
    return render(request, "quizzes/deleteQs.html", context)


def updateText(request, id):
    context ={}
    obj = get_object_or_404(Question, id = id)
 
    # pass the object as instance in form
    form = QuestionUpdateTextForm(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
    return render(request, "quizzes/updateQId.html", context)

def updateType(request, id):
    context ={}
    obj = get_object_or_404(Question, id = id)
 
    # pass the object as instance in form
    form = QuestionUpdateTypeForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "quizzes/updateQId.html", context)


def updateQuestion(request, id):
    context ={}
    obj = get_object_or_404(Question, id = id)
 
    # pass the object as instance in form
    form = QuestionUpdateForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "quizzes/updateQId.html", context)