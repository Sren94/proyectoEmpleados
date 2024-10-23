from django import forms

class newDepartamentoForm(forms.Form):
    firstName = forms.CharField(max_length=50)
    lastName=  forms.CharField(max_length=50)
    depName=  forms.CharField(max_length=50)
    shortName= forms.CharField(max_length=20)
    