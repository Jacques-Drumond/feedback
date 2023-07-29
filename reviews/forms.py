from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField(max_length= 100, required=True, min_length=10, error_messages={
        "required": "Username can't be blank."
    })