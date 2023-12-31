from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('register/', views.userRegister, name="register"),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
    path('account/', views.userProfile, name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),

    path('create-skill/', views.createSkill, name='create-skill'),
    path('update-skill/<str:pk>', views.updateSkill, name='update-skill'),
    path('delete-skill/<str:pk>', views.deleteSkill, name='delete-skill'),
]
