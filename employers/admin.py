from django.contrib import admin
from .models import Employer


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ['name', 'verification_code', 'is_verified',
                    'phone_number', 'created', 'updated',]

    readonly_fields = ['name', 'verification_code', 'company',
                       'company_location', 'company_telephone', 'email', 'phone_number']
