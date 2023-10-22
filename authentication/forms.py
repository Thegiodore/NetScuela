from django import forms
from .models import SignUp, Login


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
