from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorials
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def home(request):
    return render(request=request,
                  template_name='new_app/home.html',
                  context={'tutorials': Tutorials.objects.all}

                  )


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('new_app:homepage')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request,
                  "new_app/register.html",
                  context={'form': form})