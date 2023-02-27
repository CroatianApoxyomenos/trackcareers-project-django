from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


job_title = [
    "First job",
    "Second job"
]

job_description = [
    "First job description",
    "Second job description"
]

# Create your views here.

def job_list(request):
    list_of_jobs = "<ul>"
    for job in job_title:
        job_id = job_title.index(job)+1
        detail_url = reverse('jobs_detail', args=(job_id,))
        list_of_jobs += f"<li>{job} <a href={detail_url}>here</a></li>"
    list_of_jobs += "</ul>"
    return HttpResponse(list_of_jobs)

def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        return_html = f"<h1>{job_title[id-1]}</h1> <h3>{job_description[id-1]}</h3>"
        return HttpResponse(return_html)
    except:
        return HttpResponseNotFound("Not found")