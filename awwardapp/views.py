from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from django.contrib .auth import logout
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'index.html')


def logoutUser(request):
    logout(request)
    return redirect('index')   