from django import forms
#from django.core.exceptions import ValidationError
class LoginForm(forms.Form):
   username=forms.CharField(max_length=30)
   email=forms.EmailField(max_length=30)
