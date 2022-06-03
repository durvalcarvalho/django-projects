from django.urls import path

from profiles import views

app_name = 'profiles'


urlpatterns = [
    path('my/', views.MyProfileView.as_view(), name='my-profile-view'),

    path(
        'unfollowed/',
        views.UnfollowedProfiles.as_view(),
        name='unfollowed-profiles',
    ),
]
