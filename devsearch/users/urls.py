from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('register-page/', views.userRegister, name="register-page"),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
]
