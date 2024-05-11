from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import JobPost

job_title = [
    "first job",
    "second job",
    "third job"
]

job_description = [
    "first job description",
    "second job description",
    "third job description"
]

# Create your views here.

# def hello(request):
#     return HttpResponse("<title> Home </title> <h2>Hellow world</h2>")

class TempClass:
    x = 5



def hello(request):
    list = ["alpha", "Beta"]
    temp = TempClass()
    is_authenticated = False
    context = {"name":"Django", "firstList":list, "temp_obj":temp, "age":10
                ,"is_authenticated":is_authenticated}
    # return HttpResponse(template.render(context, request))
    return render(request, "app/hello.html", context)

def job_list(request):
    # list_of_jobs = "<ul>"
    for j in job_title:
        job_id = job_title.index(j)
        detail_url = reverse("jobs_detail", args=(job_id,))
    #     list_of_jobs += f"<li><a href='{detail_url}'>{j}</a></li>"
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)

    jobs = JobPost.objects.all()
    context = {"jobs":jobs}
    return render(request, "app/index.html", context)

def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse("jobs_home"))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        context = {"job_title":job_title[id], "job_description":job_description[id]}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")