from profiles.models import Profile


def profile_pic(request):
    context = { 'profile_url': None }

    if request.user.is_authenticated:
        context['profile_url'] = request.user.profile.avatar.url

    return context


def number_of_received_invites(request):
    context = { 'number_of_received_invites': 0 }
    if request.user.is_authenticated:
        profile = request.user.profile
        context['received_invitations_num'] = profile.get_number_of_received_invitations()

    return context