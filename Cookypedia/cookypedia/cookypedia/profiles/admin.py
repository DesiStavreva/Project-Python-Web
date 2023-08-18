from django.contrib import admin

from cookypedia.profiles.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'profile_image', 'age')
    list_per_page = 10
    list_filter = ('age',)
