from django.contrib import admin

from debtors.models import Debtor


class DebtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'debt', 'user', 'updated_at', 'created_at',)
    list_filter = ('user',)
    search_fields = ('name',)
    ordering = ('-updated_at',)

admin.site.register(Debtor, DebtorAdmin)