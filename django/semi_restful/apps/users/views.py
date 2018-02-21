from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

def base(req):
    return redirect('/users')

def index(req):
    context = {
        "all_users": User.objects.all()
    }
    return render(req, 'users/index.html', context)

def new(req):
    return render(req, 'users/new.html')

def edit(req, num):
    context = {
        "id": num
    }
    return render(req, 'users/edit.html', context)

def show(req, num):
    user = User.objects.get(id=num)
    context = {
        "id": num,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "created_at": user.created_at,
        "updated_at": user.updated_at
    }
    return render(req, 'users/show.html', context)

def create(req):
    errors = User.objects.basic_validator(req.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error)
        return redirect('/users/new')
    else:
        User.objects.create(first_name=req.POST["first_name"], last_name=req.POST["last_name"], email=req.POST["email"])
        new_id = User.objects.last().id
    return redirect('/users/{}'.format(new_id))

def destroy(req, num):
    user = User.objects.get(id=num)
    user.delete()
    return redirect("/users")

def update(req):
    errors = User.objects.basic_validator(req.POST)
    user_id = int(req.POST["id"])
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error)
        return redirect('/users/{}/edit'.format(user_id))
    else:
        user = User.objects.get(id = user_id)
        user.first_name = req.POST["first_name"]
        user.last_name = req.POST["last_name"]
        user.email = req.POST["email"]
        user.save()
        return redirect('/users/{}'.format(user.id))
