from django import forms
from django.contrib.auth import get_user_model
from .models import SignUp, Login

User = get_user_model()
class SignUpModelForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = [
            'firstname',
            'lastname',
            'email',
            'password1',
            'password2',
        ]


class LogInModelForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = [
            'email',
            'password',
        ]
