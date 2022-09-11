from django.db import models


# Create your models here.
class ProjectData(models.Model):
    category = models.CharField(max_length=200)
    project_name = models.CharField(max_length=400)
    description = models.TextField()
    hours = models.DecimalField(max_digits=9, decimal_places=2)
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    dollars = models.DecimalField(max_digits=9, decimal_places=2)
    record_date = models.DateField()
