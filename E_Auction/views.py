from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from .forms import NewUserForm
#from django.contrib.auth import login
#from django.contrib import message


def MainHome(request):
    return render(request, "index.html")

def aboutUs(request):
    return render(request, "about.html")

def home(request):
    return render(request, "home.html")

def random(request, random):
    return HttpResponse(random)

def contact(request):
    return render(request, "contact.html")

def register(request):
#	if request.method == "POST":
#		if form.is_valid():
#			user = form.save()
#			login(request, user)
#			messages.success(request, "Registration successful." )
#			return redirect("main_home")
#		messages.error(request, "Unsuccessful registration. Invalid information.")
#	form = NewUserForm()
#	return render (request=request, template_name="registration.html", context={"register":form})
	return render (request, "registration.html")
def login(request):
    return render(request, "login.html")