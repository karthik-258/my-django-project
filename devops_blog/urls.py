from django.urls import path
from devops_blog import views

urlpatterns = [
    path('',views.blogformview,name='blogform'),
]
