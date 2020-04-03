from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse



@login_required(login_url="/login/")
def index(request):

    return render(request, "hospitalindex.html")