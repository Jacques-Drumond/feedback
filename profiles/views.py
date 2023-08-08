from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
import os
from .functions import get_folder_size
# Create your views here.

def store_file(folder, file):
    with open(f"{folder}{file.name}.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        if get_folder_size("temp") < 4501795:
            store_file("temp/", request.FILES['image'])
        else:
            store_file("temp2/", request.FILES['image'])
        return HttpResponseRedirect("/profiles")