from rest_framework import serializers 
from .models import User 
from django.http import request 
from django.contrib import auth


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    class Meta:
        model = User
        fields = ['email','username','password']

    def validate(self,attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric xters')
        return attrs
        
    def create(self, validated_data):
        return  User.objects.create_user(**validated_data)


#for login should only ask for the email aaand after which ask user to input the otp
#custom function for sending otp
def send_otp(email):
    pass
class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255,min_length=3)

    class Meta:
        model=User 
        fields=['email']
    
    def validate(self,attrs):
        email=attrs.get('email','')
        filtered_user_by_email = User.objects.filter(email__iexact=email)
    #on validating that the user with the email exists then we have to send otp
        if filtered_user_by_email.exists():
            pass
            #trigger function to send otp to emai
            # 

