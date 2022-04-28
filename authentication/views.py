from django.shortcuts import render
from authentication.renderers import UserRenderer
from rest_framework import serializers
# Create your views here.
from rest_framework import generics,permissions,status,views 
from .serializers import*
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import Util

#view to handle user registration
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer, )

    def post(self,request):
        user=request.data 
        serializer= self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data=serializer.data
        #if u need the email the below step does it better
        user=User.objects.get(email=user_data['email'])

        #am going to use the OTP pproach for authentication
        email_body = 'Welcome to VirtuaSasa /t'+user.username+'/tPlease complete the registration'
        data = {
            'email_body':email_body,
            'to_email':user.email,
            'email_subject':'Registration successful'
        }
        Util.send_email(data)
        return Response(user_data,status=status.HTTP_201_CREATED)
