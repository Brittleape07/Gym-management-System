from dataclasses import fields
from pyexpat import model
from random import choices
from django.core import validators
from django import forms
from home.models import Equipments, Member
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class MemberRegistration(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'dob', 'occupation', 'phone', 'address', 'city', 'state', 'zip', 'plan', 'shift']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'dob' : forms.DateInput(attrs={'class':'form-control', 'type':'date'} ),
            'occupation' : forms.Select(attrs={'class':'form-control', 'class':'form-select'} ),
            'phone' : forms.NumberInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'state' : forms.TextInput(attrs={'class':'form-control'}),
            'zip' : forms.NumberInput(attrs={'class':'form-control'}),
            'plan' : forms.Select(attrs={'class':'form-control', 'class':'form-select'}),
            'shift' : forms.Select(attrs={'class':'form-control', 'class':'form-select'}),
            
            }
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EquipmentRegistration(forms.ModelForm):
    class Meta:
        model = Equipments
        fields = ['name', 'category', 'quantity']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control', 'class':'form-select'}),
            'quantity' : forms.NumberInput(attrs={'class':'form-control'}),
            
        }