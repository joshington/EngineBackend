from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status,views 
# Create your views here.
from rest_framework.views import APIView
from .models import Category,Property
from .serializers import*
from rest_framework.response import Response


#view to list all categories

class ListCategoryView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    name='category-list'


#==now the details of the category
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name='category-detail'

class CategoryProperty(generics.ListAPIView):
    serializer_class = PropertySerializer
    def get_queryset(self):
        cat_id = self.kwargs.get('pk',None)
        #print(cat_id)
        if cat_id:
            #category =  get_object_or_404(Category,id=cat_id)
            properties = Property.objects.filter(
                category_name=cat_id
            )
            return properties 
        else:
            return Property.objects.none() 
        
        
    # serializer_class=CategorySerializer
    # queryset=Category.objects.all().get_absolute_url()
#category property details
# class CategoryProperties(generics.GenericAPIView):
    # serializer_class = CategorySerializer
    # def get(self,request):
        # category = Category.objects.all()
        # properties = category.get_absolute_url()
        # return Response(properties,status=status.HTTP_200_OK)
    # serializer_class = CategorySerializer
    # queryset = Category.objects.all().get_absolute_url()
    # def get
    # now the magic starts
    # def get_queryset(self):
        # cat_id = self.request.query_params.get('pk')
        # if cat_id:
            # category = get_object_or_404(Category,cat_id)
            # properties =  Property.objects.filter(
            #    category_name=category.category_name 
            # ).all()
            # return properties
        # else:
            # return an erroar
            # return
            # got abad request

#implementing a search functionality maybe later
class PropertyDetailView(generics.RetrieveAPIView):
    queryset=Property.objects.all()
    serializer_class = PropertySerializer
