from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        verify_email = all_clean_data["verify_email"]

        if email != verify_email:
            raise forms.ValidationError("Email and verify email must be matching!!!!")


