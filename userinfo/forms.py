from django import forms


class RegForm(forms.Form):
    username = forms.CharField(label='please enter you name')
    password = forms.CharField(label='please enter you password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='please enter you password again', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 6:
            raise forms.ValidationError('it is too short')
        return username
