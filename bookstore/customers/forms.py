from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


INPUT_FIELD_STYLING = "form-input py-1 px-2 rounded-3 border-0"


class CustomerForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter username", "class": INPUT_FIELD_STYLING}
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your first name", "class": INPUT_FIELD_STYLING}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your last name", "class": INPUT_FIELD_STYLING}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter your email", "class": INPUT_FIELD_STYLING}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password", "class": INPUT_FIELD_STYLING}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password again ", "class": INPUT_FIELD_STYLING}
        )
    )
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter username", "class": INPUT_FIELD_STYLING}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password", "class": INPUT_FIELD_STYLING}
        )
    )
