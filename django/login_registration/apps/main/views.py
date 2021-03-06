# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from .models import User

def index(req):
    return render(req, "main/index.html")

def register(req):
    errors = User.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, errors[error])
        return redirect('/')
    else:
        User.objects.create(first_name=req.POST["first_name"], last_name=req.POST["last_name"], email=req.POST["email"], password=bcrypt.hashpw(req.POST["password"].encode(), bcrypt.gensalt()))
        user = User.objects.last()
        req.session["id"] = user.id
        return redirect('/success')

def login(req):
    try:
        user = User.objects.get(email=req.POST["email"])
    except:
        messages.error(req, "Email not found.")
        return redirect('/')

    if bcrypt.checkpw(req.POST["password"].encode(), user.password.encode()):
        req.session["id"] = user.id
        return redirect('/success')
    else:
        messages.error(req, "Invalid password.")
        return redirect('/')

def success(req):
    user = User.objects.get(id=req.session["id"])
    context = {
        "name": user.first_name
    }
    return render(req, "main/success.html", context)

def clear(req):
    all_users = User.objects.all()
    for user in all_users:
        user.delete()
    return redirect('/')
