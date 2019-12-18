from django.urls import path
from devops_blog import views

app_name = 'devops_blog'

urlpatterns = [
    path('blogform/',views.blogformview,name='blogform'),
    path('all_blogs/',views.all_blogsview,name='all_blogs'),
    path('thankyou/',views.thankyouview,name='thankyou'),
    path('git/',views.gitview,name='git'),
    path('jenkins/',views.jenkinsview,name='jenkins'),
    path('ansible/',views.ansibleview,name='ansible'),
    path('buildtools/',views.buildtoolsview,name='buildtools'),
    path('cloud/',views.cloudview,name='cloud'),
    path('datascience/',views.datascienceview,name='datascience'),
    path('docker/',views.dockerview,name='docker'),
    path('kubernates/',views.kubernatesview,name='kubernates'),
    path('linux/',views.linuxview,name='linux'),
    path('machinelearning/',views.machinelearningview,name='machinelearning'),
    path('monitoringtools/',views.monitoringtoolsview,name='monitoringtools'),
    path('python/',views.pythonview,name='python'),
]
