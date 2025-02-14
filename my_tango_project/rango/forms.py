from django import forms
from rango.models import Category, Page
from django import forms
from django.contrib.auth.models import User
from rango.models import UserProfile
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category._meta.get_field('name').max_length, help_text="Please enter the category name.")

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page._meta.get_field('title').max_length, help_text="Please enter the page title.")
    url = forms.URLField(help_text="Please enter the URL.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        fields = ('title', 'url')

    def clean(self):
        cleaned_data = super().clean()
        url = cleaned_data.get('url')
        if url and not url.startswith('http://') and not url.startswith('https://'):
            cleaned_data['url'] = 'http://' + url
        return cleaned_data
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')