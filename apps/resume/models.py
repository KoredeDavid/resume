from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='resume/project_images/')
    url = models.URLField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=25, unique=True)
    rank = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name
