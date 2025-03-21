from django.urls import path
from . import views
from accounts.views import user_login  # Import from accounts
from .views import home
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path("home/", home, name="home"),
    path('logout/', views.logout_user, name='logout'),
]
