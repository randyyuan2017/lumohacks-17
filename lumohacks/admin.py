from lumohacks.models import *
from django.contrib import admin


class PetUserAdmin(admin.ModelAdmin):
    model = PetUser
    list_display = ('auth_user',)


class PetAdmin(admin.ModelAdmin):
    model = Pet
    list_display = ('name',)

class ConnectionAdmin(admin.ModelAdmin):
    model = Connection


class GiftAdmin(admin.ModelAdmin):
    model = Gift
    list_display = ('name','auth_user',)
    raw_id_fields = ['auth_user']

class ActivityAdmin(admin.ModelAdmin):
    model = Activity
    list_display = ('description',)


class UserActivitiesAdmin(admin.ModelAdmin):
    model = UserActivities
    raw_id_fields = ['activity']

admin.site.register(PetUser, PetUserAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Gift, GiftAdmin)
admin.site.register(Connection, ConnectionAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(UserActivities, UserActivitiesAdmin)