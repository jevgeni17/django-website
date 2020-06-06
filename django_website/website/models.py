from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=1000, db_index=True)
    link = models.TextField(blank=True, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    

    def __str__(self):
        return self.title