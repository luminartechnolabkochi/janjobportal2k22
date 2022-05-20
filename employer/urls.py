from django.contrib import admin
from employer import views
from django.urls import path
urlpatterns = [
path("home",views.EmployerHomeView.as_view(),name="emp-home"),
    path("jobs/add",views.AddJobView.as_view(),name="emp-addjob")
]