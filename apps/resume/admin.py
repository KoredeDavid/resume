from django.contrib import admin

# Register your models here.

from .models import Project, Skill

# Register your models here.

admin.site.register(Project)
admin.site.register(Skill)