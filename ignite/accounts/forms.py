from multiprocessing import AuthenticationError
from django import forms
from django.shortcuts import get_object_or_404
from .models import Friend_Request, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class userCreate(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'first_name', 'last_name',
                   'email', 'profile_picture',
                   'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign Up!', css_class='btn-secondary'))

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    profile_picture = forms.FileField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'profile_picture']

class addFriend(forms.Form):
    username = forms.CharField(max_length=100, label="Username",help_text="Enter your friends username" )

class FriendRequests(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(FriendRequests, self).__init__(*args, **kwargs)
        current_user = get_object_or_404(User, username=user)
        self.fields['requests'] = forms.ModelChoiceField(queryset= Friend_Request.objects.filter(to_user=current_user), to_field_name="id")

    class Meta:    
        fields = ('requests', )

class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'username or email',
            }
        )
    )

    password = forms.CharField(
        label='', 
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'password'
            }
        )
    )