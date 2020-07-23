import time

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator

from faceverifier.models import UserDetails, UserImages


class LoginForm(forms.Form):
    email = forms.EmailField(label="", max_length=50, validators=[EmailValidator],
                             widget=forms.TextInput(attrs={"class": "form-control mb-10", "placeholder": "Your Email"}
                                                    )
                             )
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        "class": "form-control mb-10", "placeholder": "Your password"
    }))


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", max_length=50, validators=[EmailValidator],
                             widget=forms.TextInput(attrs={"class": "form-control mb-10", "placeholder": "Your Email"}
                                                    )
                             )
    first_name = forms.CharField(label="", max_length=50,
                                 widget=forms.TextInput(
                                     attrs={"class": "form-control mb-10", "placeholder": "Your First Name"}
                                     )
                                 )

    last_name = forms.CharField(label="", max_length=50,
                                widget=forms.TextInput(
                                    attrs={"class": "form-control mb-10", "placeholder": "Your Last Name"}
                                )
                                )
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        "class": "form-control mb-10", "placeholder": "Your Password"
    }))

    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        "class": "form-control mb-10", "placeholder": "Confirm Password"
    }))

    class Meta:
        model = UserDetails
        fields = {'email', 'first_name', 'last_name', 'password1', 'password2'}


class CreateUserImageForm(forms.ModelForm):
    client_id = forms.CharField(label="", max_length=50, widget=forms.TextInput
    (attrs={'class': 'form-control', 'placeholder': 'employee_id, student_id, customer_id'}
     )
    )

    class Meta:
        model = UserImages
        widgets = {
            'user_id': forms.HiddenInput(),
        }
        fields = ['client_id',
                  'image']
