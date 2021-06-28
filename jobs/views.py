from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from jobs.models import Job, Cities, JobTypes


def jobList(request):
    job_list = Job.objects.order_by('job_type')
    template = loader.get_template('jobList.html')
    context = {'job_list': job_list}

    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JobTypes[job.job_type][1]

    return HttpResponse(template.render(context))


def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("job does not exist")

    return render(request, 'job.html', {'job': job})
