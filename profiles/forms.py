from django import forms

class profileForm(forms.Form):
    user_image = forms.ImageField(allow_empty_file=False)