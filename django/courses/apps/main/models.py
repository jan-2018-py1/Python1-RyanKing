from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData["name"]) <= 5:
            errors["name"] = "Course name must be more than 5 characters."
        if len(postData["description"]) <= 15:
            errors["description"] = "Description must be more than 15 characters."
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
