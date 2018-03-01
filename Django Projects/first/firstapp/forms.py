from django import forms
from .models import Topic, Userprofile
from django.contrib.auth.models import User


# class Userprofileform(forms.ModelForm):
#     portfolio = forms.URLField(required=False)
#     picture = forms.ImageField(required=False)
#
#     class Meta:
#         model = Userprofile
#         exclude = ('user',)

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfo(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ('portfolio', 'picture')


class AddTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class Webform(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)
    reenter_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        rpassword = all_clean_data['reenter_password']

        if password != rpassword:
            raise forms.ValidationError('password doesnt match')
        return all_clean_data
