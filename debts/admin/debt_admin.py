from django.contrib import admin

from debts.models.debt_model import Debt


class DebtAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'debt', 'debtor',)
    list_filter = ('debtor',)
    search_fields = ('description',)
    ordering = ('created_at',)

admin.site.register(Debt, DebtAdmin)