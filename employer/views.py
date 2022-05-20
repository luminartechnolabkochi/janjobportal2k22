from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
#List,Detail,Update,Delete,

class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"


# space_bar
# an