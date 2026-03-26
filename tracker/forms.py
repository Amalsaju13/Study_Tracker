from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudyEntry


class StudyEntryForm(forms.ModelForm):

    study_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = StudyEntry
        fields = [
            "topic",
            "study_date",
            "progress",
            "description",
            "notes"
        ]

        widgets = {
            'topic': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter study topic'
            }),

            'hours': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Hours studied'
            }),

            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write notes...'
            }),
        }


class SignupForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']