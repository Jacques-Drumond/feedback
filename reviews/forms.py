from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'reiview_text', 'rating']

        labels = {
            fields[0]: "Name",
            fields[1]: "Feedback",
            fields[2]: "Rating",
        }
        error_messages = {
            fields[0]: {
                "required": "Your name can't be empty.",
                "max_length": "Please enter a shorter name!"
            },
            fields[1]: {
                "required": "We want your feedback!"
            },
            fields[2]: {
                "required": "Give your rating"
            },
        }