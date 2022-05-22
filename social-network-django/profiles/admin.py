from django.contrib import admin

from profiles.models import Profile, Relationship

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    class Meta:
        model = Relationship


