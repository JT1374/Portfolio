
# Imports.
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Forms for user_auth.
class RegisterForm(UserCreationForm):
    """
    Form for user registration.
    """
    
    first_name = forms.CharField(max_length=30, required=True)
    
    
    class Meta:
        """
        Meta class for the form.
        """
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')