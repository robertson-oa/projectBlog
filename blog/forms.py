from django import forms
from django.forms import SelectDateWidget
from .models import BlogEntry,Category,Tags,Comment,Post,CustomUser
from django.contrib.auth.models import User
from django.forms import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')



class PostForm(forms.ModelForm):
    publication_date = forms.DateTimeField(widget=SelectDateWidget())
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['slug']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ['slug']



class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        #fields = ['username','email','password','gender','profile_pic','profile_desc']
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ['username', 'email', 'password']
        fields = '__all__'