from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from profiles.models import Profile, Relationship
from profiles import forms


@login_required
def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)

    form = forms.ProfileModelForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=profile
    )

    successfully_updated = False

    if request.method == 'POST' and form.is_valid():
        form.save()
        successfully_updated = True

    context = {
        'profile': profile,
        'form': form,
        'successfully_updated': successfully_updated,
    }

    return render(request, 'profiles/my_profile.html', context)

class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        received_invitations = self.request.user.profile.invitations_received.all()
        sent_invitations     = self.request.user.profile.invitations_sent.all()

        received_users = [inv.sender.user for inv in received_invitations]
        sent_users     = [inv.receiver.user for inv in sent_invitations]

        context['invitations_received'] = received_users
        context['invitations_sent'] = sent_users

        context['posts'] = self.object.get_public_posts()

        return context


@login_required
def profile_detail_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    context = { 'profile': profile, }

    return render(request, 'profiles/profile_detail.html', context)


@login_required
def invites_received_view(request):
    invitations = request.user.profile.get_invitations_received()
    senders = [invitation.sender for invitation in invitations]

    context = {
        'senders': senders,
    }

    return render(request, 'profiles/my_invites.html', context)


@login_required
def profiles_list_view(request):
    profiles = Profile.objects.get_all_profiles(user=request.user)

    context = {
        'profiles': profiles,
    }

    return render(request, 'profiles/profiles_list.html', context)


@login_required
def invite_profiles_view(request):
    profiles = Profile.objects.get_all_profiles_to_invite(profile=request.user.profile)

    context = {
        'profiles': profiles,
    }

    return render(request, 'profiles/invite_profiles.html', context)


class ProfileListView(LoginRequiredMixin, generic.ListView):
    model = Profile
    template_name = 'profiles/profiles_list.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.get_all_profiles(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user.profile

        print('\n'*3)
        print('profile', profile)
        print('\n'*3)

        # context['invitations_received'] = profile.invitations_received
        # context['invitations_sent'] = profile.invitations_sent

        received_invitations = profile.invitations_received.all()
        sent_invitations     = profile.invitations_sent.all()

        received_users = [inv.sender.user for inv in received_invitations]
        sent_users     = [inv.receiver.user for inv in sent_invitations]

        context['invitations_received'] = received_users
        context['invitations_sent'] = sent_users

        return context


@login_required
def send_cancel_invitation_view(request):
    if request.method != 'POST':
        return redirect('profiles:profiles-list-view')

    pk = request.POST.get('profile_pk')
    invitation_type = request.POST.get('invitation_type')

    sender = request.user.profile
    receiver = get_object_or_404(Profile, pk=pk)

    rel, created = Relationship.objects.get_or_create(
        sender=sender,
        receiver=receiver,
        defaults={ 'status': Relationship.StatusChoices.SENT },
    )

    if invitation_type == 'cancel-friendship-request':
        rel.delete()

    return redirect('profiles:profiles-list-view')


@login_required
def accept_reject_invitation_view(request):
    if request.method != 'POST':
        return redirect('profiles:profiles-list-view')

    pk = request.POST.get('profile_pk')

    receiver = request.user.profile
    sender = get_object_or_404(Profile, pk=pk)

    rel = Relationship.objects.get(sender=sender, receiver=receiver)

    if 'accept-invitation' in request.POST:
        rel.status = Relationship.StatusChoices.ACCEPTED
        rel.save()

    elif 'reject-invitation' in request.POST:
        rel.delete()

    return redirect(request.META.get('HTTP_REFERER'))
    # return redirect('profiles:profiles-list-view')


@login_required
def remove_from_friends_view(request):
    if request.method != 'POST':
        return redirect('profiles:profiles-list-view')

    pk = request.POST.get('profile_pk')

    profile_1 = request.user.profile
    profile_2 = get_object_or_404(Profile, pk=pk)

    rel = Relationship.objects.get(
        Q(sender=profile_1, receiver=profile_2) |
        Q(sender=profile_2, receiver=profile_1)
    )

    rel.delete()

    return redirect('profiles:profiles-list-view')
