from django.urls import path
from . import views

app_name = 'baseapp'
urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.LoginPage,name='login'),
    path('register/',views.register,name='register'),
    path('welcome/',views.welcome,name='welcome'),
    path('logout/',views.LogoutPage,name='logout'),
    path('api/course/',views.CourseView.as_view(),name='course'),
    path('api/getcourses',views.getcourses,name='getcourses')
]
