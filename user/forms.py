from django import forms
from .models import CustomUser
import re

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth', 'avatar']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].label = "Change Avatar"

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            if not re.match(r'^\d{9}$', phone_number):
                raise forms.ValidationError('Please enter the last 9 digits of your Ukrainian phone number.')
            return f'+380{phone_number}'
        return phone_number
