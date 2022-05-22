from django.shortcuts import redirect, render
from profiles.models import Profile

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


def signup_view(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        # It's need to save to post_save signal create profile
        new_user = form.save()

        if ref_profile_id := request.session.get('ref_profile_id', None):
            ref_profile = Profile.objects.get(id=ref_profile_id)
            new_user.profile.recommended_by = ref_profile.user
            new_user.profile.save()

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('main-view')

    context = { 'form': form, }
    return render(request, 'signup.html', context)


def main_view(request):
    if ref_code := request.GET.get('ref_code', None):
        print(f'Ref code: {ref_code}')
        if profile := Profile.objects.filter(code=ref_code).first():
            request.session['ref_profile_id'] = profile.id
            print(f'Profile: {profile}')
    context = {}
    return render(request, 'main.html', context)