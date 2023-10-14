from django.db import models
import secrets


def verify_code():
    return f'jinho-{secrets.token_hex(5)}'.upper()


class Employer(models.Model):
    name = models.CharField('Employer\'s name', max_length=255, unique=True)
    verification_code = models.CharField(max_length=25, default=verify_code, unique=True)
    company = models.CharField('Orgainzation\'s name', max_length=255)
    company_location = models.CharField(
        'Orgainzation\'s location', max_length=255)
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(
        'Employer Phone Number', max_length=15, unique=True)
    company_telephone = models.CharField(
        'Company Phone Number', max_length=15, unique=True)
    email = models.EmailField('Employer\'s email', max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
