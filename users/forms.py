from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skills, Message


class RegsiterPageForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')
        widgets = {
            'password': forms.PasswordInput(attrs={
                'placeholder': 'create password'
            })
        }

    # def save(self, commit=True):
    #     user = super().save(commit)
    #     user.set_password(self.cleaned_data['password'])
    #     user.save()
    #     return user


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'email', 'username', 'short_intro', 'bio', 'loacation', 'profile_image',
                  'socail_github', 'socail_youtube', 'socail_twiter', 'socail_linkedin', 'socail_website')


class AddSkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('name', 'description')


class EditSkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('name', 'description')


class SendMassegesForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name','email','subject','body')
