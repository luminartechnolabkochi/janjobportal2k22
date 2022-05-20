from django.db import models

# Create your models here.


class Jobs(models.Model):
    job_title_name=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    location=models.CharField(max_length=120)
    salary=models.PositiveIntegerField(null=True)
    experience=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.job_title_name
#print all jobs where experience > 1

#python3 manage.py makemigrations
#python3 manage.py migrat

# Modelname.objects.create(field=value,field=value,,,,)
#Jobs.objects.create(job_title_name="front end developer"
# ,company_name="tcs",location="kakkand",salary=25000,experience=4)

#qs=Jobs.objects.all()

# employees
#Employees(ename,salary,dept,exp)
#emp create
#fetch all employees
#filter


# fetching a specific object

# qs=Jobs.objects.get(id=5)
# print qs

#Create=>mpodename.objevts.create(f=v)
#all=> mn.objects.all()
#mn.objects.get(uf=value)
#qs=Jobjs.objects.filter(company_name="ey")
#Create
#List
#Detail
#Update
#delete