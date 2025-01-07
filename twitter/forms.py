from django import forms


gender = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
    ("Prefer not to say", "Prefer not to say")
)
class TwitterRegistrationForm(forms.Form):
    firstname = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    c_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    
class UserProfileForm(forms.Form):
    dob = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    gender = forms.ChoiceField(label="Gender", choices=gender, widget=forms.RadioSelect(attrs={'class':'from-control'}))
    profile_img = forms.ImageField(label="Profile Picture", widget=forms.FileInput)
    
    