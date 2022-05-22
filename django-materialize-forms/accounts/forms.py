from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if not user or not user.check_password(password):
                raise forms.ValidationError(
                    "Wasn't able to log you in with those credentials."
                )

            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")

        return super().clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username')

    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')

    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            'password2',
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError(
                'This username is already being used.'
            )
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        qs = User.objects.filter(email=email)

        if qs.exists():
            raise forms.ValidationError(
                'This email is already being used.'
            )

        return email

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2 != password:
            raise forms.ValidationError("Passwords must match.")

        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError("Emails must match.")

        return super().clean(*args, **kwargs)


