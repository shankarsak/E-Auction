from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    fname = forms.CharField(max_length=50)
    lname = forms.CharField(max_length=50)
    contact = forms.IntegerField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields =("fname", "lname", "contact", "username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.fname= self.cleaned_data['fname']
        user.lname= self.cleaned_data['lname']
        user.contactail= self.cleaned_data['contact']
        user.email= self.cleaned_data['email']
        if commit:
            user.save()
        return user