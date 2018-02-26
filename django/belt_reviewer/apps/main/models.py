from __future__ import unicode_literals

from django.db import models
import re

class UserManager(models.Manager):
    def validate(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        errors = {}
        if len(postData["name"]) < 2:
            errors["name"] = "Name must be at least 2 letters."

        if len(postData["alias"]) < 2:
            errors["alias"] = "Alias must be at least 2 letters."

        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Invalid email format."
        elif len(User.objects.filter(email=postData["email"])):
            errors["email"] = "Email already exists in database."

        if len(postData["password"]) < 8:
            errors["password"] = "Password must be at least 8 characters."
        elif postData["password"] != postData["confirm"]:
            errors["password"] = "Passwords don't match."

        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")

class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, related_name="reviews")
    user = models.ForeignKey(User, related_name="reviews")
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
