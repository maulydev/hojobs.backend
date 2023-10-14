from rest_framework.serializers import ModelSerializer
from .models import Job
from category.serializers import CategorySerializer


class JobSerializer(ModelSerializer):
    # job_category = CategorySerializer()

    class Meta:
        model = Job
        fields = '__all__'
