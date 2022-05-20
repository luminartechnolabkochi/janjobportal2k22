from django import forms

class JobForm(forms.Form):
    job_title_name=forms.CharField()
    company_name=forms.CharField()
    location=forms.CharField()
    salary=forms.IntegerField()
    experience=forms.IntegerField()

