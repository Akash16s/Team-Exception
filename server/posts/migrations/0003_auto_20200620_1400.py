# Generated by Django 3.0.7 on 2020-06-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('posts', '0002_postmodel_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, to='groups.groupModel'),
        ),
    ]