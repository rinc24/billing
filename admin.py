from django.contrib import admin
from .models import Account, Operation, PromoCode


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'balance')
    readonly_fields = ('balance',)


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('time', 'value', 'reason', 'details', 'account', 'balance')
    readonly_fields = ('time', 'value', 'account', 'balance')


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('promo', 'cost', 'code', 'is_used', 'owner')
    readonly_fields = ('code', 'is_used')
