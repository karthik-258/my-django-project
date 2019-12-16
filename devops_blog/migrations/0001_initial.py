# Generated by Django 2.2.7 on 2019-12-15 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('G', 'GIT'), ('J', 'JENKINS'), ('B', 'BUILD TOOLS'), ('D', 'DOCKER'), ('A', 'ANSIBLE'), ('K', 'KUBERNATES'), ('C', 'CLOUD'), ('L', 'LINUX'), ('P', 'PYTHON'), ('S', 'DATA SCIENCE'), ('M', 'MACHINE LEARNING'), ('O', 'MONITORING TOOLS')], max_length=20)),
                ('author_name', models.CharField(max_length=60)),
                ('article_name', models.CharField(max_length=150)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
