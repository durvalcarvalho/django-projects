from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from accounts.forms import UserLoginForm, UserRegisterForm

User = get_user_model()


def login_view(request):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password'),
        )

        login(request, user)

        if next_page := request.GET.get('next'):
            return redirect(next_page)

        return redirect('/')

    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)

        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(
            username=user.username,
            password=password,
        )

        login(request, new_user)

        if next_page := request.GET.get('next'):
            return redirect(next_page)

        return redirect('preferences:my-preference-add-view')

    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('preferences:my-preference-add-view')