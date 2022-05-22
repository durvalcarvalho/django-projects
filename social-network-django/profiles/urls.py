from django.urls import path

from profiles import views

app_name = 'profiles'


urlpatterns = [
    path('my/', views.my_profile_view, name='my-profile-view'),

    # path('<int:pk>/', views.profile_detail_view, name='profile-detail-view'),
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail-view'),

    path('invites/', views.invites_received_view, name='invites-received-view'),

    path(
        '',
        # views.profiles_list_view,
        views.ProfileListView.as_view(),
        name='profiles-list-view',
    ),

    path('invite-profiles/', views.invite_profiles_view, name='invite-profiles-view'),

    path(
        'send-cancel-invitation/',
        views.send_cancel_invitation_view,
        name='send-cancel-invitation-view',
    ),

    path(
        'accept-reject-invitation/',
        views.accept_reject_invitation_view,
        name='accept-reject-invitation-view',
    ),

    path(
        'remove-friendship/',
        views.remove_from_friends_view,
        name='remove-friendship-view',
    ),
]