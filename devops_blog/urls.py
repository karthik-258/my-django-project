from django.urls import path
from devops_blog import views

app_name = 'devops_blog'

urlpatterns = [
    path('blogform/',views.blogformview,name='blogform'),
    path('all_blogs/',views.all_blogsview,name='all_blogs'),
    path('thankyou/',views.thankyouview,name='thankyou'),
    path('git/',views.gitview,name='git')
]
