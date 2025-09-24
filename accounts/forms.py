from  django import forms
from .models import CustomUser
from django.forms import widgets as widget 

class SchoolAdminRegistrationForm(forms.Form):
    username = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'input w-full p-2 '}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input w-full p-2 '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input w-full p-2 '}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input w-full p-2 '}))

    first_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'input w-full p-2 '}))
    last_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'input w-full p-2 '}))
    phone_number=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'input w-full p-2 '}))
    address = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'input w-full p-2 '}))
    profile_pic=forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'input-file w-full p-2'}),required=False)

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise forms.ValidationError("Passwords do not match")

    def save(self, commit=True):
        user = CustomUser(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            phone_number=self.cleaned_data['phone_number'],
            address=self.cleaned_data['address'],
            profile_pic=self.cleaned_data['profile_pic']
        )
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class SchoolAdminLoginForm(forms.Form):
    username = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'input w-full p-2 '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input w-full p-2 '}))
    