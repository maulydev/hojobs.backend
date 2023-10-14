from django.db import models
from category.models import Category
import secrets


class Job(models.Model):

    JOB_TYPE = (
        ('Open', 'Open',),
        ('Full-time', 'Full-time',),
        ('Part-time', 'Part-time',),
        ('Contract', 'Contract',),
        ('Internship', 'Internship',),
        ('NSS Internship', 'NSS Internship',),
    )

    id = models.TextField(
        primary_key=True, default=secrets.token_urlsafe, editable=False)
    verification_code = models.CharField(max_length=20, default="", null=True, blank=True)
    title = models.CharField('Job title', max_length=255)
    job_type = models.CharField(
        'Job type', choices=JOB_TYPE,  max_length=15, default="Open")
    job_category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name='job_category', to_field='title')
    description = models.TextField('Job description')
    company = models.CharField('Company name', max_length=255)
    location = models.CharField('Job location', max_length=255)
    salary = models.CharField('Salary', max_length=50, default='Not stated')
    requirements = models.TextField(
        'Qualification & Experience', default='Not applicable')
    application_method = models.CharField('How to apply', max_length=255)
    closing_date = models.DateField('Closing date')
    is_active = models.BooleanField('Active status', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.title
