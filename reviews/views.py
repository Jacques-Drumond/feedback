from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# retorna o form
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


# retorna a pag /thank-you
class thankYouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['message'] = 'This Works'

        return context

# retorna a lista 
class reviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self) -> QuerySet[Any]:
        base_query = super().get_queryset()
        base_query = base_query.order_by('rating')
        
        return base_query
# retorna a pag
class reviewDetail(DetailView):
    template_name = 'reviews/review_details.html'
    model = Review
