from django.db import models
from django.contrib.auth.models import User

# User prfile with images Authication
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Profile-pics")
    
    

    
    
