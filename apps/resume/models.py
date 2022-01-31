from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125)
    image = models.ImageField(upload_to='resume/project_images/')
    url = models.URLField()

    def __str__(self):
        return self.name

