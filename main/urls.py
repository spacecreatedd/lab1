from django.urls import path, include
from . import views
from .views import profile

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),

    #Страница регистрации
    path('profile/', views.profile, name="profile"),
    path('login/', views.LoginUserView.as_view(), name="login"),
    path('register/', views.RegisterUserView.as_view(), name="register"),
    path('logout/', views.logout_view, name="logout")
]
