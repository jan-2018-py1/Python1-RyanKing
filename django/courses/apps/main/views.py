from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import Course, CourseManager

def index(req):
    # Course.objects.create(name="first class", description="this is the first class")
    context = {
        "all_courses": Course.objects.all()
    }
    return render(req, 'main/index.html', context)

def add(req):
    errors = Course.objects.validate(req.POST)
    if len(errors):
        for error in errors:
            print errors[error]
            messages.error(req, errors[error])
        return redirect('/')
    else:
        Course.objects.create(name=req.POST["name"], description=req.POST["description"])
        return redirect('/')

def destroy(req, num):
    context = {
        "course": Course.objects.get(id=num)
    }
    return render(req, 'main/destroy.html', context)

def delete(req, num):
    course = Course.objects.get(id=num)
    course.delete()
    return redirect('/')
