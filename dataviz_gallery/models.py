from django.db import models

# Create your models here.


class Plot(models.Model):
    parent_name = models.CharField(max_length=200, default="No plot name available")
    variation_name = models.CharField(max_length=200, default="No plot name available", primary_key=True)
    synonyms = models.CharField(max_length=200, default="No synonyms")
    goals = models.CharField(max_length=200, default="No goals available")
    dimensionality = models.CharField(max_length=200, default="No dimensionality info available")
    numerical = models.CharField(max_length=200)
    categorical = models.CharField(max_length=200)
    visual_cues = models.CharField(max_length=200, default="No visual cue info available")
    coordinate_system = models.CharField(max_length=200, default="No coordinate system info available")
    shapes = models.CharField(max_length=200, default="No shape info available")
    description = models.TextField(default="No description available")
    anatomy = models.TextField(default="No anatomy info available")
    caveats = models.TextField(default="No caveat info available")
    facetted = models.BooleanField()
    single_facetted = models.BooleanField()
    dual_facetted = models.BooleanField()
    grouped = models.BooleanField()
    plot_package = models.CharField(max_length=200, default="No plot package info available")
    related = models.CharField(max_length=200, default="No info for related plot available")
    implemented = models.BooleanField(default=False)
    icon = models.FilePathField(path="img/icon/")
    seaborn = models.FilePathField(path="img/seaborn/")
