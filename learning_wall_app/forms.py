from django import forms

from .models import User


class PostForm(forms.Form):
    post_body = forms.CharField(label='Your name', max_length=250)


class RegisterForm(forms.ModelForm):
    name= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username',)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return username

    def clean_password2(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def clean_name(self):
    	print "+++++++++"
    	return self.cleaned_data.get("name")


class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
