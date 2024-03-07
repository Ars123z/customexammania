from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from .models import UserProfile
from django import forms



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['city', 'state', 'country', 'standard', 'phone_no'] 