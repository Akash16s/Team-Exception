# Generated by Django 3.0.7 on 2020-06-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0002_postmodel_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='compModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='comp/')),
                ('desc', models.TextField(blank=True)),
                ('link', models.TextField()),
                ('contact', models.TextField()),
                ('Tags', models.ManyToManyField(to='posts.tagModel')),
            ],
        ),
    ]
