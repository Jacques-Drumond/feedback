from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
import os
from .functions import get_folder_size, store_file
from .forms import profileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
# Create your views here.

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"