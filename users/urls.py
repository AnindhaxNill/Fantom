
from django.urls import path,include
from .views import *


app_name = "users"
urlpatterns = [
    path("register/",RegisterView.as_view()  ,name="register"),
    path("login/",UserLoginView.as_view()  ,name="login"),
    path("logout/",UserLogoutView.as_view()  ,name="logout"),
   
]
