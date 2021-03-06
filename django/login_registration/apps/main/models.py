from __future__ import unicode_literals

from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def validate(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        errors = {}
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name must be at least 2 letters."
        elif not postData["first_name"].isalpha():
            errors["first_name"] = "First name must only contain letters."

        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name must be at least 2 letters."
        elif not postData["last_name"].isalpha():
            errors["last_name"] = "Last name must only contain letters."

        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Invalid email format."
        elif len(User.objects.filter(email=postData["email"])):
            errors["email"] = "Email already exists in database."

        if postData["password"] != postData["confirm"]:
            errors["password"] = "Passwords don't match."

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
