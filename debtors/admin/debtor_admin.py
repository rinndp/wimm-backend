from django.contrib import admin

from debtors.models import Debtor


class DebtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'debt', 'user',)
    list_filter = ('user',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Debtor, DebtorAdmin)