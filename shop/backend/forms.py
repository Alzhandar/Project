from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):

    def clean_price(self):
        value=self.cleaned_data['price']
        if value<0:
            raise Exception('Not valid')
        return value
    class Meta:
        model = Product
        fields = ['name', 'desc', 'price', 'stock', 'category']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']