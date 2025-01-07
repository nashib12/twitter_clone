from django.shortcuts import render, redirect
from .forms import TwitterRegistrationForm
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.

def home(request):
    return render(request, "home.html")


# ------------------------- User registration and login part  ------------------------- 

def registration(request):
    forms = TwitterRegistrationForm()
    if request.method == "POST":
        forms = TwitterRegistrationForm(request.POST)
        if forms.is_valid():
            f_name = forms.cleaned_data["firstname"]
            l_name = forms.cleaned_data["lastname"]
            u_name = forms.cleaned_data["username"]
            email = forms.cleaned_data["email"]
            password = forms.cleaned_data["password"]
            c_password = forms.cleaned_data["c_password"]
            
            if password == c_password:
                User.objects.create_user(first_name=f_name, last_name=l_name,username=u_name,email=email,password=password)
                return redirect("user_profile")
    return render(request, "authintication/registration.html", {"forms":forms})


def user_profile(request):
    return render(request, "authintication/user_profile.html")
            


