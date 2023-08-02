from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View

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
def thank_you(request):
    return render(request, 'reviews/thankyou.html', )