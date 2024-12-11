from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already taken.")
        return email
    
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class BoshmenuForm(forms.ModelForm):
    class Meta:
        model = Boshmenu
        fields = ['name','image']


class BookatableForm(forms.ModelForm):
    class Meta:
        model = Bookatable
        fields = ['name','phone','date','time','people']

        filds = {
            'date': forms.DateInput(attrs={'type': 'date'}),  
            'time': forms.TimeInput(attrs={'type': 'time'}), 
        }


class GetintouchForm(forms.ModelForm):
    class Meta:
        model = Getintouch
        fields = ['name','email','message',]

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','image','malumoti',]

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['date','teacher','language','location']

class RsForm(forms.ModelForm):
    class Meta:
        model = Reserveyourspotdetailsmenutecher
        fields = ['name','details','teacher','category']
 

class GiveagifeForm(forms.ModelForm):
    class Meta:
        model = Giveagift
        fields = ['name','image','price','text']


class LatestnewsrForm(forms.ModelForm):
    class Meta:
        model = Latestnews
        fields = ['name','image','text','date']

class NewrestuarantForm(forms.ModelForm):
    class Meta:
        model = Newrestuarant
        fields = ['name','image','text',]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','image','price']