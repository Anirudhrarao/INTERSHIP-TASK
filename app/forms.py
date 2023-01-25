from django import forms
from .models import User


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password','password2','profile','is_doctor','is_patient','line1','city','state','pincode')

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password2")
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
                )
        