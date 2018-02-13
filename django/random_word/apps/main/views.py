from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if "attempts" not in request.session:
        request.session["attempts"] = 0
    return render(request, "main/index.html")

def generate(request):
    request.session["word"] = get_random_string(length=14)
    request.session["attempts"] += 1
    return redirect('/')

def reset(request):
    del request.session["attempts"]
    return redirect('/')
