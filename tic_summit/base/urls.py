from django.urls import path, include
from .views import login_user, signup, logout_user, home

urlpatterns = [
    path('home/', home, name="home"),
    path('signin/', login_user, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
]
