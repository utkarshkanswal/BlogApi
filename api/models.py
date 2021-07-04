from django.db import models
from froala_editor.fields import FroalaField
import uuid

# Create your models here.


class User(models.Model):
    _id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=False)
    phone = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=False)
    linkedin_profile = models.URLField(max_length=100)


class Blog(models.Model):
    _id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=200)
    content = models.JSONField(default="")
