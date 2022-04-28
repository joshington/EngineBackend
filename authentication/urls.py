from django.urls import path 
from .views import*

app_name='authentication'

urlpatterns = [
    path('register/',RegisterView.as_view(), name="register"),
]
