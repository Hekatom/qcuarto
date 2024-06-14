from django import forms
from django.db import models
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

# Extendemos del original
class RegistrationForm(forms.ModelForm):
    #phone = PhoneNumberField(
    #    label=('Teléfono'),
    #    required=True,
    #    widget=
    #    ),
    #    strip=True
    #)
    
    class Meta:
        model = CustomUser
        fields = ["username",
            "email",
            "phone", 
            "password1", 
            "password2"]
        
        #phone = PhoneNumberField(widget=PhoneNumberPrefixWidget, required = True)

        widgets = {  
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre o apodo'}),
		    'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email',}),
		    'phone': PhoneNumberPrefixWidget(attrs={'class': 'form-control','placeholder':'Numero de telefono'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Repita contraseña'}),
        
             }


#    def save(self, commit=True):
#        user = super(RegistrationForm, self.save(commit=False))
#        user.email = cleaned_data['email']
#
#        if commit:
#            user.save()
#
 #       return user
