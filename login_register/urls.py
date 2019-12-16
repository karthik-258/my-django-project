from django.urls import path
from login_register import views

app_name = 'login_register'

urlpatterns = [
    
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),

]
