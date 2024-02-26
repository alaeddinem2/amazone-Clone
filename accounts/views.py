from django.shortcuts import render,redirect
from .forms import SignupForm, ActivationForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save()  

            profile = Profile.objects.get(user__username=usernme)
            send_mail(
                    "Account Activation",
                    f"hi {username}\n you code activation is :{profile.code}",
                    "from@example.com",
                    [email],
                    fail_silently=False,
                    )
            return redirect('accounts/username/activate')

    else:
        form = SignupForm()

    return render(request, 'registration/register.html', {'form': form})
    


def activate(request,username):
    pass