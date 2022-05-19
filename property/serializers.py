#from attr import fields
from rest_framework import serializers 
from .models import Category,Property,Image 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =  '__all__'


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property 
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image 
        fields = '__all__'

    