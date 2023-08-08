from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
import os
from .functions import get_folder_size, store_file
from .forms import profileForm
from .models import UserProfile
# Create your views here.

class CreateProfileView(View):

    def get(self, request):
        form = profileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })
    
    def post(self, request):

        submitted_form = profileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()
            return HttpResponseRedirect("/profiles")
        else:
            return render(request, "profiles/create_profile.html", {
                "form": submitted_form
            })