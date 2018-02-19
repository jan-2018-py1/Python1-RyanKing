from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def register(req):
    return HttpResponse("Placeholder for users to create a new user record")

def login(req):
    return HttpResponse("Placeholder for users to log in")

def users(req):
    return HttpResponse("Placeholder to later display the list of users")
