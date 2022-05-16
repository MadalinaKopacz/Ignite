from multiprocessing import context
import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

def main(request):
    url = "/accounts/login"
    context = {"login_link" : url}
    return render(request,"global/index.html", context=context)