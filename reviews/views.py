from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView
from reviews.form import ReviewForm
from reviews.models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'
    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, 'reviews/review.html', {
    #         'form': form
    #     })
    #
    # def post(self, request):
        # To edit an existing entry
        # from reviews.models import Review
        # data_to_delete = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance=data_to_delete)
        # form = ReviewForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return HttpResponseRedirect('/thank-you')
        # return render(request, 'reviews/review.html', {
        #     'form': form
        # })


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context


class ReviewsListView(ListView):
    template_name = 'reviews/reviews_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context


class ReviewDetailView(DetailView):
    template_name = 'reviews/review_details.html'
    model = Review

    # To modify the variable, otherwise default is model name in lowercase or object
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['id']
    #     review = Review.objects.get(pk=review_id)
    #     context['review'] = review
    #     return context

