from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

from app.models import JobPost

job_title = [
    "First job",
    "Second job",
    "Third job",
]

job_description = [
    "First job description",
    "Second job description",
    "Third job description"
]


# Create your views here.
class TempClass:
    x = 5


def hello(request):
    list = ["alpha", "beta"]
    is_authenticated = False
    context = {"name": "George", "first_list": list, "temp_object": TempClass(), "age": 25, "is_authenticated": is_authenticated}
    return render(request, 'app/hello.html', context)


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