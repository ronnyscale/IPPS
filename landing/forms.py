from django import forms
from core.models import Person

passwordInputWidget = {
    "password": forms.PasswordInput(),
}


class LoginForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["username", "password"]
        widgets = [passwordInputWidget]
