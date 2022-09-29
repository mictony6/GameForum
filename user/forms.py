from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
import re


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2",)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        # check for digit
        if not len(re.findall('\d', password)) >= 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password1', msg)

        # check for uppercase letter

        if not re.findall('[A-Z]', password):
            msg = 'Password must contain at least 1 uppercase letter.'
            self.add_error('password1', msg)
    # check for 1 symbol
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            msg = "Password must contain at least 1 symbol."
            self.add_error('password1', msg)

        password_confirm = cleaned_data.get('password2')

        if password and password_confirm:
            if password != password_confirm:
                msg = "The two password fields must match."
                self.add_error('password2', msg)

        return cleaned_data
