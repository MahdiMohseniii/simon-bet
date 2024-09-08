from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label= "",
        max_length= 50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your name'})
    )

    last_name = forms.CharField(
        label= "",
        max_length= 50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your last name'})
    )

    email = forms.EmailField(
        label="",
        max_length= 50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your email address'})
    )
    username = forms.CharField(
        label= "",
        max_length= 20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your User Name'})
    )
    
    phone_number = forms.CharField(
        label= "",
        max_length= 22,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your phone number'})
    )

    location = forms.CharField(
        label= "",
        max_length= 50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your location'})
    )

    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'Enter more than 8 chars'
            }
        )
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'Enter more than 8 chars'
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'phone_number', 'location', 'password1', 'password2' )
