from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from profiles.models import Profile


class MyProfileView(generic.DetailView):
    model = Profile
    template_name = 'profiles/my_profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset.get(user=self.request.user)


class UnfollowedProfiles(generic.View):
    def get(self, request):
        profile = request.user.profile
        unfollowed_profiles = profile.get_unfollowed_profiles()
        data = {'profiles': [profile.to_json() for profile in unfollowed_profiles]}
        return JsonResponse(data)
