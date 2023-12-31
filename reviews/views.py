from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm, linkForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

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

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context['is_favorite'] = favorite_id == str(loaded_review.id)
        return context
    
class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
    

class insertLinkView(View):
    def get(self, request):
        form_class = linkForm
        return render(request, 'reviews/image_downloader.html', {
            "form": form_class
        })
    def post(self, request):
        link = request.POST['link']
        soup = BeautifulSoup(urlopen(link).read(), features="html.parser")
        link = soup.find(itemprop="image")
        print(link)  
        return HttpResponseRedirect('image-downloader')