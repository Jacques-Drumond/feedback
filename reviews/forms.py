from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField(max_length= 100, required=True, min_length=10, error_messages={
        "required": "Username can't be blank."
    })
    review_text = forms.CharField(label="Feedback", widget=forms.Textarea, max_length=300, min_length=10)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)