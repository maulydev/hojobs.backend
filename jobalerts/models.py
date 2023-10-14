from django.db import models


class Subscription(models.Model):
    email = models.EmailField('Subscriber email', unique=True)
    category = models.CharField('Job Category', max_length=255)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField('Date of subscription', auto_now_add=True)
    updated = models.DateTimeField('Date of subscription modification', auto_now=True)

    
    def __str__(self) -> str:
        return self.email