from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth import login, authenticate
from .models import Profile
from django.contrib import messages
from store.utils import cartData
from store.models import Product


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
    id_ = request.user.id
    user_profile = get_object_or_404(Profile, user=id_)
    form = ProfileForm(instance=user_profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()

            if request.FILES.get('image', None) != None:
                print(request.FILES)
                user_profile.image = request.FILES['image']
                user_profile.save()
                messages.success(request, 'Profile was updated successfully!')
            return redirect('ProfilePage')

    messages.warning(request,'Profile was not updated successfully!' )
    return render(request, "users/profile_update.html", {'form': form})
