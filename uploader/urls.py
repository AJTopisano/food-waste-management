from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('posts/', views.posting, name='posting'),
    path('viewpost/<int:pk>', views.viewpost,name='viewpost'),
    path('addpost', views.addpost,name='addpost'),
    path('delete/<int:pk>', views.deleteblog,name='delete'),
    path('register/',views.registerpage,name='register'),
    path('login/', views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('login1/',views.loggin,name='loggin'),
    path('homee/', views.homee,name='homee'),
    
]