from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorials
# Create your views here.

def home(request):
    return render(request=request,
                  template_name='new_app/home.html',
                  context={'tutorials': Tutorials.objects.all}

                  )
