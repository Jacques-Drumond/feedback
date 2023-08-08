from django import forms

class profileForm(forms.Form):
    user_image = forms.FileField(allow_empty_file=False)