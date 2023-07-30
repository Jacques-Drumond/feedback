from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
def index(request):
    # se a requisição for POST. 
    if request.method == "POST":
        # instancia o formulário com os dados da requisição.
        form = ReviewForm(request.POST)
        
        # verifica se o formulário é valido (parâmetros configurados no forms).
        if form.is_valid():
            print(form.cleaned_data)

            # instancia na variável os dados coletados do formulário, as keys vem do 
            # models user_name, review etc.
            review = Review(
                user_name=form.cleaned_data['username'],
                reiview_text=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating']
            )
            # utiliza o método de modelo save() para salvar no database
            review.save()
            # redireciona para a pagina /thank-you fazendo com que a função thank_you rode.
            return HttpResponseRedirect('/thank-you')
        
    # se a requisição não for POST
    else:
        # instancia o form sem dados, só a base, o cód HTML etc.
        form = ReviewForm()

    # retorna a pagina /review com a base do formulário.
    return render(request, 'reviews/review.html', {
        "form": form
    })

# retorna a pag /thank-you
def thank_you(request):
    return render(request, 'reviews/thankyou.html', )