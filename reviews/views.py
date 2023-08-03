from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review

class ReviewView(View):
    def get(self, request):
        
        form = ReviewForm()

        return render(request, 'reviews/review.html', {
            "form": form
        })
    
    def post(self, request):

        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, 'reviews/review.html', {
            "form": form
        })


# retorna a pag /thank-you
class thankYouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['message'] = 'This Works'

        return context


class reviewsListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        context['reviews'] = Review.objects.all()

        return context