from django.urls import path
from core.views import *

urlpatterns = [
    path('', PostView.as_view(), name="home"),
]
