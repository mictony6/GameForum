from django.urls import path
from user.views import *


urlpatterns = [


    path("signup/", UserCreateView.as_view(), name="signup"),

]
