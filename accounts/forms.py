from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



# community = forms.ChoiceField(initial=1, choices=((1, 'None'), (2, 'LCOS'), (3, 'LMOS'), (4, 'Lords of the Pit'), (5, 'El Norte No Olvida'), (6, 'LIOS')))
