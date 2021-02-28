from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate


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
            user = authenticate(request, username=username, password=password, first_name=first_name,last_name=last_name)
            if user is not None:
                login(request, user)
            return redirect('Store')
    return render(request, 'users/create.html', {'form': form})
