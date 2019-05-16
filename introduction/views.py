from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MessageForm, UserForm, LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):

    context = {
        'Course_name': 'Python',
        'Date_created' : '1990',
        'Language_level' : 'high-level',
        'Programming_paradigm':'object-oriented',
        'interpreted_or_compiled' : 'interpreted',
        'advantages' : 'readability, automatic memory management, support of multiple programming paradigms',


    }

    return render(request, 'introduction/home.html', context)


def tableofcontents(request):



    return render(request, 'introduction/tableofcontents.html')


def contactus(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'introduction/message.html', {'form': form})

    else:
        form = MessageForm()
        return render(request, 'introduction/message.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password =raw_password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'introduction/tableofcontents.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    else:
        form = UserForm()
        return render(request, 'introduction/registration.html', {'form': form})


def login_func(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'introduction/tableofcontents.html')
                else:
                    return HttpResponse('Disabled account')

            else:
                return HttpResponse('Invalid login')

    else:
        form = LoginForm()
        return render(request, 'introduction/login.html', {'form':form})


def functions(request):
    return render(request, 'introduction/functions.html')



def exceptions(request):
    return render(request, 'introduction/exceptions.html')



def decisionmaking(request):
    return render(request, 'introduction/decisionmaking.html')

def agile(request):
    return render(request, 'introduction/agile.html')

def scrum(request):
    return render(request, 'introduction/scrum.html')

def kanban(request):
    return render(request, 'introduction/kanban.html')

def docker(request):
    return render(request, 'introduction/docker.html')

def gitcontrol(request):
    return render(request, 'introduction/gitcontrol.html')

def kubernetes(request):
    return render(request, 'introduction/kubernetes.html')


def cicd(request):
    return render(request, 'introduction/cicd.html')





