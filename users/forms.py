from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django import forms
from users.models import Tasks

class Regform(UserCreationForm):
    password2= forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username","email",]

class loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,"class":"form-control"}))
    password = forms.CharField(label=("Password"),strip=False,
               widget=forms.PasswordInput(attrs={"autocomplete": "current-password","class":"form-control"}),
    )

class Taskform(forms.ModelForm):
      class Meta:
        model=Tasks
        fields=["title","description","complete"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "complete":forms.CheckboxInput(attrs={"class":"form-control"}),
                 }
