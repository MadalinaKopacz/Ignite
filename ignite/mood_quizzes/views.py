from multiprocessing import context
import random
import re
from django.http import HttpResponse
from django.shortcuts import render
from .forms import QuestionCreateForm, QuestionUpdateForm, QuestionUpdateTextForm, QuestionUpdateTypeForm, QuizForm
from .models import Question
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from activities.views import chooseActivities
from start_page.views import get_temperature

# Create your views here.
def createView(request):
    context = {}
    form = QuestionCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, "quizzes/createquestion.html", context)

def get_quiz(request):
    temp = get_temperature(request)["description"]
    if request.method =="POST":
        # Use data to get activity
        print(request.POST)
        return chooseActivities(request, socialScore = request.POST['answer1'],
                        physicalScore= request.POST['answer2'], moneyScore=request.POST['answer3'], weather=temp, counter=0)
        
        # return HttpResponse("cv")

    questions = Question.objects.all()
    type1 = questions.filter(qtype = 1)
    type2 = questions.filter(qtype = 2)
    type3 = questions.filter(qtype = 3)


    n1 = len(type1)
    n2 = len(type2)
    n3 = len(type3)

    context = {'q1':type1[random.randint(0, n1-1)],
                'q2':type2[random.randint(0, n2-1)],
                'q3':type3[random.randint(0, n3-1)]}
    
     # pass the object as instance in form
    form = QuizForm()
 
    # add form dictionary to context
    context["form"] = form
    return render(request, "quizzes/quiz.html", context)

def listView(request):
    context ={}
 
    context["dataset"] = Question.objects.all()
         
    return render(request, "quizzes/readquestion.html", context)

def questionsByType(request, qtype):
    context ={}
 
    context["dataset"] = Question.objects.filter(qtype = qtype)
         
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

def deleteQuestionsByType(request, qtype):
    context ={}
 
 
    if request.method =="POST":
        Question.objects.filter(qtype = qtype).delete()
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