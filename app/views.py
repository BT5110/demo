from django.shortcuts import render

from .models import Greeting


def index(request):
    context = {'nbar': 'home'}
    return render(request, 'index.html', context)


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()
    context = {'greetings': greetings, 'nbar': 'db'}
    return render(request, 'db.html', context)


def tpc_c(request):
    context = {'nbar': 'tpc-c'}
    return render(request, 'tpc-c.html', context)


def project(request):
    context = {'nbar': 'project'}
    return render(request, 'project.html', context)
