from django.urls import path
from .views import home, registration, user_profile

urlpatterns = [
    path("",home,name="home"),
    
    # ---------------- authintication ---------------- 
    path("registration/",registration,name="registration"),
    path("user_profile/",user_profile,name="user_profile"),
]
