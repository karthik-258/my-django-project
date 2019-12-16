from django.db import models

# Create your models here.
class blogmodel(models.Model):
    MAIN_TOPICS = (
        ('G', 'GIT'),
        ('J', 'JENKINS'),
        ('B', 'BUILD TOOLS'),
        ('D', 'DOCKER'),
        ('A', 'ANSIBLE'),
        ('K', 'KUBERNATES'),
        ('C', 'CLOUD'),
        ('L', 'LINUX'),
        ('P', 'PYTHON'),
        ('S', 'DATA SCIENCE'),
        ('M', 'MACHINE LEARNING'),
        ('O','MONITORING TOOLS')
    )
    type = models.CharField(max_length=20, choices=MAIN_TOPICS)
    author_name = models.CharField(max_length=60)
    article_name = models.CharField(max_length=150)
    date_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    content = models.TextField()
