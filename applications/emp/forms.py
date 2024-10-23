#importar el modulo de forms
from django import forms
from .models import employee
class employeeForm(forms.ModelForm):
    
    class Meta:
        model = employee
        fields = (
            'firstName',
            'lastName',
            'email',
            'skill',
            'dep',
            'job'
            )
        class Meta():
            model=employee
            fields = (
            
            )
        widgets={
            'firstName': forms.TextInput(
                attrs={
                    'placeholder':'Ejemplo: juan'
                },
            ),
            'lastName': forms.TextInput(
                attrs={
                    'placeholder':'Ejemplo: juan'
                }
            ),
            'email': forms.TextInput(
                attrs={

                    'placeholder':'Ejemplo: juanPerez@ejemplo.com'
                }
            ),
            'skill':forms.CheckboxSelectMultiple()        
        }

class EmpForm(forms.ModelForm):
    
    class Meta():
        model=employee
        fields = (
            
        )
        widgets={
            'firstName': forms.TextInput(
                attrs={
                    'placeholder':'Ejemplo: juan'
                },
            ),
            'lastName': forms.TextInput(
                attrs={
                    'placeholder':'Ejemplo: juan'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder':'Ejemplo: juanPerez@ejemplo.com'
                }
            ),
            'shortName': forms.TextInput(
                attrs={
                    'placeholder':'Ejemplo: Dep De Redes'
                }
            )
        }