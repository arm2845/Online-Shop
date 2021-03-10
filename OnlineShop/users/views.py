from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth import login, authenticate
from .models import Profile
from store.utils import cartData


def create(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.data.get('username')
            password = form.data.get('password1')
            first_name = form.data.get('first_name')
            last_name = form.data.get('last_name')
            user = authenticate(request, username=username, password=password, first_name=first_name, last_name=last_name)
            if user is not None:
                login(request, user)
            return redirect('Store')
    return render(request, 'users/create.html', {'form': form})


def profile_page(request):
    profile = Profile.objects.get(user=request.user.id)
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems, 'profile': profile}
    return render(request, "users/profile.html", context)


def profile_update(request):
    profile = Profile.objects.get(user=request.user.id)
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            if request.FILES.get('image', None) != None:
                print(request.FILES)
                profile.image = request.FILES['image']
                profile.save()

            return redirect('ProfilePage')

    data = cartData(request)
    cartItems = data['cartItems']

    return render(request, "users/profile_update.html", {'cartItems': cartItems, 'form': form})