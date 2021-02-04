from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm,  UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(user=user)

    context = {
        'section': 'dashboard',
        "profile_pic": profile.photo.url
    }
    return render(request,
                  'account/dashboard.html',
                  context)

@login_required
def home(request):

    context = {
        
    }
    return render(request,
                  'home.html',
                  context)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
  # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
 # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
 # Save the User object
            
            Profile.objects.create(user=new_user)

            return render(request,
                            'account/register_done.html',
                            {'new_user': new_user})
        
       
    else:
        user_form = UserRegistrationForm()
    return render(request,
                    'account/register.html',
                    {'user_form': user_form})


@login_required
def edit(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, 
                                    data=request.POST)

        profile_form = ProfileEditForm(
                                        instance=user,
                                        data=request.POST,
                                        files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            # profile_form.save()
            
            Profile.objects.create(
                user=user,
                date_of_birth=profile_form.cleaned_data["date_of_birth"],
                photo=profile_form.cleaned_data["photo"]
            )
    else:
        user_form = UserEditForm(instance=request.user)
        # profile = Profile.objects.get(user=user)
        profile_form = ProfileEditForm(
                                    instance=user)
    return render(request,
                        'account/edit.html',
                        {'user_form': user_form,
                        'profile_form': profile_form})