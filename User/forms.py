from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserAccount, AdaptPet

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
   
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        new_user = super().save(commit=False)
        if commit == True:
            new_user.save()
            UserAccount.objects.create(
                user = new_user,
                account_no = 241100 + new_user.id
            )
        return new_user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class DepositMoney(forms.ModelForm):
    amount = forms.IntegerField()
    class Meta:
        model = UserAccount
        fields = ['amount']

class UpdateUser(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
