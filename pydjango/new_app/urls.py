from django.urls import path
from . import views

app_name = 'new_app'

urlpatterns = [
    path('', views.home, name='home'),
    path("register", views.register, name='register')
]