from django.contrib import admin

from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'is_staff', 'is_superuser', 'is_active')
    list_editable = ('is_staff', 'is_superuser', 'is_active')

    list_filter = ('is_staff', 'is_superuser', 'is_active',)
    search_fields = ('email',)
    ordering = ('-updated_at',)

admin.site.register(CustomUser, CustomUserAdmin)
