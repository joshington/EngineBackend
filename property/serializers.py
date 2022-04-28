#from attr import fields
from rest_framework import serializers 
from .models import Category,Property

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =  '__all__'


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property 
        fields = '__all__'