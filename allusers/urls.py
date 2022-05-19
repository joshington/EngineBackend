from django.urls import path 
from .views import*

app_name='allusers'




urlpatterns = [
    path('register-user/',CreateClientView.as_view(), name="register-user"),
    path('register-company/',RegisterCompany.as_view(), name="register-company"),
    path('login-company/',LoginCompany.as_view(), name="login-company"),
    path('companies/<int:pk>/',CompanyDetailView.as_view(), name="company-details"),
]
