from django.shortcuts import render,redirect
from .forms import SignupForm, ActivationForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save()  

            profile = Profile.objects.get(user__username=username)
            send_mail(
                    "Account Activation",
                    f"hi Mr {username}\n your activation code on RAQIB DEMO is: {profile.code}",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                    )
            return redirect(f'/accounts/{username}/activate')

    else:
        form = SignupForm()

    return render(request, 'registration/register.html', {'form': form})
    


def activate(request,username):
    profile = Profile.objects.get(user__username=username)
    user = profile.user
    if request.method == 'POST':
        form = ActivationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code :
                profile.code = ''
                profile.save()
                user.is_active = True
                user.save()
                return redirect('/accounts/login')
    else:
        form = ActivationForm()

    return render(request,'registration/activate.html',{'form':form})