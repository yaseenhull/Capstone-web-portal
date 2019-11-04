# Authors; Yaseen Hull, Laeeq Diedericks, Thobeka Gumede
# Project; Capstone SITPG
# Date; September 2019

from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileForm, StatusForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # grab username if valid stored in form.cleaned_data dictionary
            # messages.success(request, "Account created for %s " % ({{username}}))
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


@login_required
def profile(request):
    return render(request, 'profile_form.html')


def home(request):
    return render(request, 'student_home.html')


def cover(request):
    return render(request, 'cover.html')


def withdrawal(request):
    exists = False
    try:
        profile = request.user.profile
        exists = True
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if exists:

       if profile.status == 'Application has been withdrawn':
            return render(request, 'student_home.html')

       else:

           if request.method == 'POST':
                data = Profile.objects.filter(user=request.user)
                data.update(status='Application has been withdrawn')
                data.update(comment='N/A')
                data.update(evaluator='N/A')
                return redirect('student_home')

           else:
               return render(request, 'delete_form.html')
    else:
        return render(request, 'student_home.html')


def edit_profile(request):
    exists = False
    try:
        profile = request.user.profile
        status = profile.status
        exists = True
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if exists:
        if status == 'Application has been withdrawn' or status == 'Application is successful' or status == 'Application is unsuccessful':
            return render(request, 'student_home.html')
        else:
            if request.method == 'POST':
                form = ProfileForm(request.POST, request.FILES, instance=profile)

                profile.status = 'Application in review'
                profile.comment = 'Awaiting evaluation'
                profile.evaluator = 'Awaiting evaluation'
                if form.is_valid():
                    form.save()
                    return redirect('student_home')
            else:
                form = ProfileForm(instance=profile)

                return render(request, 'profile_form.html', {'form': form})

    else:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)

            profile.status = 'Application in review'
            profile.comment ='Awaiting evaluation'
            profile.evaluator='Awaiting evaluation'
            if form.is_valid():

                form.save()
                return redirect('student_home')
        else:
            form = ProfileForm(instance=profile)

            return render(request, 'profile_form.html', {'form': form})


def profile_status(request):
    data = Profile.objects.filter(user=request.user)

    pro = {"profile_data": data}
    return render(request, 'status_form.html', pro)







