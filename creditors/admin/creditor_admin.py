from django.contrib import admin

from creditors.models.creditor_model import Creditor


class CreditorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'credit', 'user', 'updated_at', 'created_at',)
    list_filter = ('user',)
    search_fields = ('name',)
    ordering = ('-updated_at',)

admin.site.register(Creditor, CreditorAdmin)