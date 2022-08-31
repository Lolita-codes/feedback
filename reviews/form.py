from django import forms


# class ReviewForm(forms.Form):
#     username = forms.CharField(label='Your Username',
#                                max_length=50,
#                                error_messages={
#                                    'required': 'This field must not be empty!',
#                                    'max_length': 'Please enter a shorter name!'
#                                })
#     review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea, max_length=250)
#     rating = forms.IntegerField(label='Your Rating', max_value=5, min_value=1)
from reviews.models import Review


# Creates a form using the model
class ReviewForm(forms.ModelForm):
    class Meta:
        # points to the model to get the fields from
        model = Review
        # to include all the fields
        fields = '__all__'
        # exclude = ['owner_comment']
        labels = {
            'username': 'Your Username',
            'review_text': 'Your Feedback',
            'rating': 'Your Rating'
        }
        error_messages = {
            'username': {
                'required': 'This field must not be empty!',
                'max_length': 'Please enter a shorter name!'
            }
        }
