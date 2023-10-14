from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Job, JobSerializer
from employers.models import Employer
from category.models import Category
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def job_list(request):
    job_type = request.query_params.get('type', None)
    job_category = request.query_params.get('category', None)

    filtered_jobs = Job.objects.filter(job_type=job_type).all(
    ) if job_type else Job.objects.filter(job_category=job_category).all()

    pg = PageNumberPagination()
    pg.page_size = 5
    try:
        if job_type or job_category:
            jobs = filtered_jobs
        else:
            jobs = Job.objects.filter(is_active=True).all()
        result_page = pg.paginate_queryset(jobs, request)
        serializer = JobSerializer(result_page, many=True)
    except Exception as e:
        return Response({'Error': str(e)})
    return pg.get_paginated_response(serializer.data)


@api_view(['GET'])
def job_detail(request, pk):
    try:
        job = Job.objects.get(pk=pk)
        serializer = JobSerializer(job)
    except Job.DoesNotExist:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def post_job(request):
    vcode = request.data.get('veriCode')
    vcode = '' if not vcode else vcode
    active_state = False

    job_category = Category.objects.get(
        title=request.data.get('jobCategory'))

    if vcode != '':
        emp = Employer.objects.filter(verification_code=vcode)
        if len(emp) != 0:
            vcode = vcode
        else:
            return Response({'warning': 'invalid verification code!'}, status=status.HTTP_404_NOT_FOUND)
        active_state = True if len(emp) != 0 else False

    new_job = Job.objects.create(
        verification_code=vcode,
        title=request.data.get('jobTitle'),
        job_type=request.data.get('jobType'),
        job_category=job_category,
        description=request.data.get('description'),
        company=request.data.get('companyName'),
        location=request.data.get('jobLocation'),
        salary=request.data.get('salary'),
        requirements=request.data.get('requirements'),
        application_method=request.data.get('howToApply'),
        closing_date=request.data.get('closingDate'),
        is_active=active_state,
    )

    try:
        if Job.objects.get(pk=new_job.id):
            return Response(status=status.HTTP_200_OK)
    except Job.DoesNotExist as not_found:
        return Response(not_found, status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def filter(request):
    job_type = request.query_params.get('type', None)
    job_category = request.query_params.get('category', None)

    filtered_jobs = Job.objects.filter(job_type=job_type).all(
    ) if job_type else Job.objects.filter(job_category=job_category).all()

    serializer = JobSerializer(filtered_jobs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
