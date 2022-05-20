from django.shortcuts import render
from django.views.generic import TemplateView,View
# Create your views here.
from employer.models import Jobs
#List,Detail,Update,Delete,
from employer.forms import JobForm
class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"


class AddJobView(View):
    def get(self,request):
        form=JobForm()
        return render(request,"emp-addjob.html",{"form":form})
    def post(self,request):
        form=JobForm(request.POST)
        if form.is_valid():
            jname=form.cleaned_data.get("job_title_name")
            cname=form.cleaned_data.get("company_name")
            location=form.cleaned_data.get("location")
            salary=form.cleaned_data.get("salary")
            exp=form.cleaned_data.get("experience")
            Jobs.objects.create(
                job_title_name=jname,
                company_name=cname,
                location=location,
                salary=salary,
                experience=exp

            )
            return render(request,"emp-home.html")
        else:
            return render(request,"emp-addjob.html",{"form":form})


# space_bar
# an