from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'reiview_text', 'rating', 'owner_comment']

        labels = {
            fields[0]: "Name",
            fields[1]: "Feedback",
            fields[2]: "Rating",
            fields[3]: "Owner comment"
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
            fields[3]: {
                "required": "Provide us your comment!"
            }
        }