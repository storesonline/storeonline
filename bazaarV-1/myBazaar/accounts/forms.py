from django import forms
from django.contrib.auth.models import User
#from .models import Profile
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','password','email','first_name','last_name']


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields =['kitchenName','cell']
