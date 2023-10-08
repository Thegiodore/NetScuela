from django import forms
from .models import SignUp, Login


class SignUpModelForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = [
            'firstname',
            'lastname',
            'email',
            'password',
        ]


class LogInModelForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = [
            'email',
            'password',
        ]
