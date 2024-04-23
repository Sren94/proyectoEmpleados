from django import forms
class newDepartamentoForm(forms.Form):
    firstName = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ejemplo:Juan'
                })
        )
    lastName = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ejemplo:Perez'
                })
        )
    email = forms.EmailField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ejemplo: juanperez@ejemplo.com'
                })
        )
    dep = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ejemplo: Seguridad y Administracion De Redes'
                })
        )
    shortName = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Seguridad De Redes'
                })
        )
        
