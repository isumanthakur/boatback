# payments/admin.py

from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'amount', 'payment_id', 'payment_status', 'created_at')
    search_fields = ('user__email', 'property__title', 'payment_id')
    list_filter = ('payment_status', 'created_at')
