# Generated by Django 3.2.6 on 2022-04-21 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_alter_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('rank', models.PositiveIntegerField(unique=True)),
            ],
        ),
    ]
