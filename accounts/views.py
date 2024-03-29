from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import SignupForm, UserForm, ProfileForm
from.models import Profile
# Create your views here.
def signup(requset):
    if requset.method=="POST":
        form = SignupForm(requset.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login (requset,user)
            return redirect('/account/profile')
    else:
        form = SignupForm
    return render(requset,'registration/signup.html',{'form':form})

def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})



def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile_edite'))

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})


