#importar el modulo de forms
from django import forms
from .models import prueba
class pruebaForm(forms.ModelForm):
    
    class Meta:
        model = prueba
        #especificando los atributos del modelo
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
        )
        #widgets son la personalizacion de los inputs del html
        widgets={
            #especificamos el campo
            'cantidad':forms.TextInput(
                #los atributos del input
                attrs={
                    'placeholder':'Ingrese Texto',
                    'class':'cantidad',
                    'id':'idCantidad'
                }
            )
        }
    def clean_cantidad(self):
        cantidad = self.cleaned_data["cantidad"]
        if (cantidad<10):
            raise forms.ValidationError('Ingrese un numero 10')
        return cantidad
        
