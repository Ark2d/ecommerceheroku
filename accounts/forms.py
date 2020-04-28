from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'phone', 'birth_date']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'phone', 'birth_date', 'is_active', 'is_staff']