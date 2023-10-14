from django.contrib import admin
from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'category', 'is_active', 'created', 'updated']
    readonly_fields = ['email', 'category']
