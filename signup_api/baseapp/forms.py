
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    company = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ("username","email","password1","password2","company")

    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        print(user)
        user.email = self.cleaned_data['email']
        user.company = self.cleaned_data['company']
        # print('message cleaned data' + self.cleaned_data)
        if commit:
            user.save()

        return user