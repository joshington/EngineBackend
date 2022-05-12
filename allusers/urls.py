from django.urls import path 
from .views import*

app_name='allusers'

urlpatterns = [
    path('register/',CreateClientView.as_view(), name="register"),
    path('register-company/',CreateCompanyView.as_view(), name="register-company"),
]
