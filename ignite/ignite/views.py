from multiprocessing import context
import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

def main(request):
    """
    method that computes the view for the start page
    """
    context = {}
    print(request.user)
    if request.user.is_anonymous:
        # make user register 😈
        return render(request,"global/index.html", context=context)
    else:
        # when user is connected redirect to page
        return HttpResponseRedirect("start_page/get")
