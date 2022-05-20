from django.contrib import admin
from employer import views
from django.urls import path
urlpatterns = [
path("home",views.EmployerHomeView.as_view(),name="emp-home")
]