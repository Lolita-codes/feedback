from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

from reviews.form import ReviewForm


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {
            'form': form
        })

    def post(self, request):
        # To edit an existing entry
        # from reviews.models import Review
        # data_to_delete = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance=data_to_delete)
        form = ReviewForm(request.POST)
        if form.is_valid():
            # review = Review(
            #     username=form.cleaned_data['username'],
            #     review_text=form.cleaned_data['review_text'],
            #     rating=form.cleaned_data['rating']
            # )
            # review.save()
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request, 'reviews/review.html', {
            'form': form
        })


def thank_you(request):
    return render(request, 'reviews/thank_you.html')
