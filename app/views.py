from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound
from django.urls import reverse
from app.models import JobPost


def job_list(request):
    jobs = JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, 'app/index.html', context)


def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        job = JobPost.objects.get(id=id)
        context = {"job": job}
        return render(request, 'app/job_detail.html', context)
    except:
        return HttpResponseNotFound("Not found")
