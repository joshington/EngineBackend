from django.core.mail import message
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status,views
from .serializers import*
from .models import Company
from django.contrib import auth

from .models import*
# Create your views here.
#==view to handle updating the user 



#==list all companies good for admin
class CompaniesListAPIView(generics.ListAPIView):
    queryset = Company.objects.all() 
    serializer_class =  CompanySerializer


#now getting the details of the specific company, just use a detail view
class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    queryset=Company.objects.all()
    serializer_class= CompanySerializer
    name='company-details'


#view for registering the company
class CreateCompanyView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CreateCompanySerializer

#==just go for the APIView style

class RegisterCompany(APIView):
    def post(self, request, *args, **kwargs):
        company_name = request.data.get('company_name')
        email  = request.data.get('email')
        password =  request.data.get('password')


        if company_name and email and password:
            company = Company.objects.filter(email__iexact=email)
            #just filter the email alone since company can have same names
            if company.exists():
                return Response({
                    'status':False,
                    'detail':'Company with email already exists'
                })
            else:
                #proceed and create the company
                reg_company = {
                    'company_name':company_name,
                    'email':email,
                    'password':password
                }  
                serializer =  CreateCompanySerializer(data=reg_company)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(
                    serializer.data 
                   
                )
        else:
            return Response({
                'status':False,
                'detail':'Provide all Details'
            }) 
        

#handling the login fucntionality of the company
class LoginCompany(APIView):
    def post(self, request,*args, **kwargs):
        email  = request.data.get('email')
        password =  request.data.get('password')

        #first ensure that user has provided both the email and password
        if email and password:
            company = Company.objects.filter(email__iexact=email)
            if company.exists():
                #proceed to work on the login functionality
                # by cecking whether password provided == password of company
                #company_rqd,created = Company.objects.get_or_create(email=email)
                company_user=authenticate(email=email,password=password)
                if company_user is not None:
                    #this user is valid
                    log_company = {
                        'email':email,
                        'password':password
                    }
                    serializer=LoginCompanySerializer(data=log_company)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    # company=auth.authenticate(email=email,password=password)

                    return Response(serializer.data,{'status':True,'detail':'Login SUccessful'})
                else:
                    return  Response({
                        'status':False,
                        'detail':'Password doesnot match'
                    })
                    #now move on guy your password is correct 
            else:
                return Response({
                    'status':'False',
                    'detail':'Account Not Found,create account'
                })
        else:
            return Response({
                'status':False,
                'detail':'Please Provide Email and Password'
            })



class UpdateProfileView(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = UpdateCompanySerializer

class CreateClientView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer