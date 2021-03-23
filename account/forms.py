from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import Portfolio


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name', )
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth',  'occupation', 'experience', 'address', 'phone', 'country', 'state', 'city', 'photo',)

class PortfolioEditForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('description',  'mywork1', 'mywork2', 'mywork3', 'mywork4', 'portfolio1', 'portfolio2', 'portfolio3', 'portfolio4',)



#     def clean_email(self):
#         if User.objects.filter(email=self.cleaned_data['email']).exists():
#             raise forms.ValidationError("the given email is already registered")
#         return self.cleaned_data['email']

# from .models import Profile
# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')


# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('date_of_birth', 'photo', 'country', 'address', 'postal_code', 'city)
