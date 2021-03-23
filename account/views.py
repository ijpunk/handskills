from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm,  UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from .models import Portfolio
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
        'profile': profile
    }
    return render(request,
                  'account/dashboard.html',
                  context)

@login_required
def home(request):
    users = User.objects.all()
    occupations = []
    all_profiles = []
    for profile in Profile.objects.all():
        if profile.get_occupation_display() not in occupations and profile.occupation.upper() != "NOT ADDED YET":
            occupations.append(profile.get_occupation_display())

    locations = []
    for profile in Profile.objects.all():
        if f'{profile.state} - {profile.city}' not in locations and f'{profile.state} - {profile.city}'.upper() != 'NONE - NONE':
            locations.append(f'{profile.state} - {profile.city}')
    profiles = Profile.objects.all()
        
    return render(request, 'home.html', {"profiles": profiles})


# def login(request):

#     context = {
        
#     }
#     return render(request,
#                   'account/login.html',
#                   context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        type = request.POST.get("type")
        print(type)
        if user_form.is_valid():
  # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
 # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
 # Save the User object
 # Save the User object
            new_user.save()
            if type == 'artisan':
                Profile.objects.create(
                    user=new_user,
                    artisan=True)
                print('ARTISAN CREATED')
            elif type == 'client':
                Profile.objects.create(
                    user=new_user,
                    client=True)


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

        portfolio_form = PortfolioEditForm(
                                        instance=user,
                                        data=request.POST,
                                        files=request.FILES)
        if user_form.is_valid() and portfolio_form.is_valid():
            user_form.save()
            # profile_form.save()
            profile = Profile.objects.get(user=user)
            if profile_form.cleaned_data["date_of_birth"]:
                profile.date_of_birth = profile_form.cleaned_data["date_of_birth"]
            if profile_form.cleaned_data["photo"]:
                profile.photo = profile_form.cleaned_data["photo"]
            if profile_form.cleaned_data["occupation"]:
                profile.occupation = profile_form.cleaned_data["occupation"]
            if profile_form.cleaned_data["experience"]:
                profile.experience = profile_form.cleaned_data["experience"]
            if profile_form.cleaned_data["phone"]:
                profile.phone = profile_form.cleaned_data["phone"]
            if profile_form.cleaned_data["address"]:
                profile.address = profile_form.cleaned_data["address"]
            if profile_form.cleaned_data["state"]:
                profile.state = profile_form.cleaned_data["state"]
            if profile_form.cleaned_data["city"]:
                profile.city = profile_form.cleaned_data["city"]
            profile.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        # profile = Profile.objects.get(user=user)
        profile_form = ProfileEditForm(
                                    instance=user)
    return render(request,
                        'account/edit.html',
                        {'user_form': user_form,
                        'profile_form': profile_form})


def profile(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(user=user)

    context = {
        'section': 'dashboard',
        "profile_pic": profile.photo.url
    }
    return render(request,
                        'account/profile.html', context)


def search_result(request):
    occupation = ''
    location = ''
    if request.GET.get('occupation'):
        occupation =  request.GET.get('occupation').upper().replace(" ", "_")
    if request.GET.get('location'):
        location =  request.GET.get('location')

    profiles = Profile.objects.filter(occupation__icontains=occupation).filter(state__icontains=location).filter(city__icontains=location)
    print(profiles)
    context = {
        "profiles": profiles
    }
    return render(request, 'account/search_result.html', context)

def single_artisan_profile(request):
    context = {
        "profiles": profiles
    }
   
    return render(request, 'account/single_artisan_profile.html', context)