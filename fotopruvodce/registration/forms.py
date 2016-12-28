
from django import forms


class Register(forms.Form):

    use_required_attribute = False

    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    url = forms.URLField(help_text="Nevyplňujte toto pole", required=False)
    signature = forms.CharField(widget=forms.HiddenInput, required=False)
    password1 = forms.CharField(min_length=6, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password1', "Hesla se neshodují")
