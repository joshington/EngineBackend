from rest_framework import serializers 
from .models import* 


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company 
        fields = '__all__'


#different serializer for creating a company
class CreateCompanySerializer(serializers.ModelSerializer):    
    class Meta:
        model= Company 
        fields = ('id','company_name', 'email','password')

    def create(self, validated_data):
        #validate the company name and 
        company = Company.objects.create(**validated_data)
        #m mostly interested in return
        #company_id = Company.objects.filter(company_name=company).latest().get().id
        #just use latest to get the last model
        #company_id = Company.objects.latest('company_name')
        return company 

    #validating email and username
    def validate(self,validated_data):
        company_name = validated_data['company_name']
        email = validated_data['email']
        if company_name and email:
            if Company.objects.filter(company_name=company_name).exists():
                raise serializers.ValidationError({"company_name":"username already in use"})
            if Company.objects.filter(email=email).exists():
                raise serializers.ValidationError({"email":"Email already in use"})
        else:
            raise serializers.ValidationError({"empty":"Add data to fields"})

        return validated_data


class LoginCompanySerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(style = { 'input_type': 'password'}, trim_whitespace = False)


    class Meta:
        model=Company
        fields=('id','email','password')

    #handling the validate issue in the serializer
    def validate(self, validated_data):
        email  = validated_data['email'].get('email','')
        password=validated_data['password'].get('email','')

        return super().validate(validated_data)





class UpdateCompanySerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = Company 
        fields = ('company_name', 'email','phone','password')


    def validate_email(self,value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email":"email already in use"})
        raise value 
        # extra_kwargs = {
        #     ''
        # }
    
    def validate_username(self,value):
        user=self.context['request'].user 
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise  serializers.ValidationError({"username": "This username is already in use."})
        return value 

    def update(self,instance, validated_data):
        #add condition for users to only update their compnay
        user = self.context['request'].user 
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize":"You dont have permission for this user"})
        instance.company_name = validated_data['company_name']
        instance.email = validated_data['email']
        instance.phone_no = validated_data['phone']
        instance.password = validated_data['password']

        instance.save()

        return instance



#now here its to help me control my user on feedback and 
# #so with that i have to make a client serializer
# 
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client 
        fields = ('id','name','emailId','countryLocation')

    def create(self, validated_data):
        client = Client.objects.create(**validated_data)
        return client 