from django.db import models

# Create your models here.


class Plot(models.Model):
    name = models.CharField(max_length=200, default="No plot name available", primary_key=True)
    # synonyme = models.CharField(max_length=200)
    # goal = models.CharField(max_length=200)
    # others_goals = models.CharField(max_length=200)
    # dimensionality = models.CharField(max_length=200)
    # shape = models.CharField(max_length=200)
    # variable_types_short = models.CharField(max_length=200)
    # variable_types_extended = models.CharField(max_length=200)
    # related = models.CharField(max_length=200)
    image = models.FilePathField(path="/img")
