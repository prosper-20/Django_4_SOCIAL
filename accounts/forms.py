from django import forms
from django.contrib.auth.models import User

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
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
    if user_form.is_valid():
        new_user = user_form.save(commit=False)
        new_user.set_password(
        user_form.cleaned_data['password'])

new_user.save()

return render(request,
'account/register_done.html',
{'new_user': new_user})
else:
user_form = UserRegistrationForm()
return render(request,
'account/register.html',
{'user_form': user_form})


from .models import Profile
# ...
class UserEditForm(forms.ModelForm):
class Meta:
model = User
fields = ['first_name', 'last_name', 'email']
class ProfileEditForm(forms.ModelForm):
class Meta:
model = Profile
fields = ['date_of_birth', 'photo']
