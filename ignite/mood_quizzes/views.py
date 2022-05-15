from django.http import HttpResponse
from django.shortcuts import render
import random

from mood_quizzes.models import Question

def get_quiz():
    questions = Question.objects.all()
    type1 = questions.filter(type == 1)
    type2 = questions.filter(type == 2)
    type3 = questions.filter(type == 3)

    n1 = len(type1)
    n2 = len(type2)
    n3 = len(type3)

    return HttpResponse([type1[random.randint(0, n1)],
                         type2[random.randint(0, n2)],
                         type3[random.randint(0, n3)]])
