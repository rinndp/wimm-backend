from django.contrib import admin

from credits.models import Credit


class CreditAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'credit', 'creditor',)
    list_filter = ('creditor',)
    search_fields = ('description',)
    ordering = ('created_at',)

admin.site.register(Credit, CreditAdmin)
