from django.db import models


class Plot(models.Model):
    parent_name = models.CharField(max_length=200, default="No plot name available")
    variation_name = models.CharField(max_length=200, default="No plot name available", primary_key=True)
    synonyms = models.CharField(max_length=200, default="No synonyme available")
    goals = models.JSONField()
    dimensionality = models.CharField(max_length=200, default="No dimensionality info available")
    numerical = models.CharField(max_length=200)
    categorical = models.IntegerField(default=0)
    visual_cues = models.JSONField()
    coordinate_system = models.JSONField()
    shapes = models.JSONField()
    description = models.TextField(default="No description available")
    anatomy = models.TextField(default="No anatomy info available")
    caveats = models.TextField(default="No caveat info available")
    facetted = models.BooleanField()
    single_facetted = models.BooleanField()
    dual_facetted = models.BooleanField()
    grouped = models.BooleanField()
    plot_package = models.CharField(max_length=200, default="No plot package info available")
    related = models.JSONField()
    implemented = models.BooleanField(default=False)
    icon = models.FilePathField(path="img/icon/")
    seaborn_plot = models.FilePathField(path="img/seaborn/")
    plotly_plot = models.FilePathField(path="img/plotly/")
    plotly_code = models.CharField(max_length=200, default="No code available")

    def __str__(self):
        return self.variation_name
