from django.core.mail import message
from django.shortcuts import redirect, render
from rest_framework import generics, permissions, status,views
from .serializers import*



from .models import*
# Create your views here.
#==view to handle updating the user 



#==list all companies good for admin
class CompaniesListAPIView(generics.ListAPIView):
    queryset = Company.objects.all() 
    serializer_class =  CompanySerializer


#view for registering the company
class CreateCompanyView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CreateCompanySerializer



class UpdateProfileView(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = UpdateCompanySerializer

class CreateClientView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer