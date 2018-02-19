from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def surveys(req):
    return HttpResponse("Placeholder to display all the surveys created")

def new(req):
    return HttpResponse("Placeholder for users to add a new survey")
