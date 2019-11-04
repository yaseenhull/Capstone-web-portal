# Authors; Yaseen Hull, Laeeq Diedericks, Thobeka Gumede
# Project; Capstone SITPG
# Date; September 2019

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Profile
from django.forms import TextInput, Select, Textarea

# the purpose of this class is so that we can add fields to our registration i.e. email field


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Student Number')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Student Number',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'surname', 'title', 'student_number', 'email_address', 'citizenship', 'country_of_origin',
                  'race', 'city_of_residence', 'country_of_residence', 'country_of_previous_institute', 'Other_country',
                  'previous_degree', 'Other_degree', 'nqf_equivalent',
                  'minimum_year_of_degree', 'previous_university', 'degree', 'years_of_IT_experience', 'math_level',
                  'math_average', 'thesis_completed_previously', 'thesis_description', 'upload']
        widgets = {
            'country_of_origin': TextInput(attrs={'class': 'international-specific'}),
            'race': Select(attrs={'class': 'sa-specific'}),
            'Other_country': TextInput(attrs={'class': 'othercountry-specific'}),
            'Other_degree': TextInput(attrs={'class': 'otherdegree-specific'}),
            'years_of_IT_experience': TextInput(attrs={'class': 'mit-specific'}),
            'math_level': Select(attrs={'class': 'mit-specific'}),
            'math_average': TextInput(attrs={'class': 'math-specific'}),
            'thesis_completed_previously': Select(attrs={'class': 'mit-specific'}),
            'thesis_description': Textarea(attrs={'class': 'project-specific'}),
        }


class StatusForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['status', 'comment', 'evaluator']


