from multiprocessing.connection import Client
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status,views,filters 
# Create your views here.
from rest_framework.views import APIView
from utils import modify_input_for_multiple_files
from .models import Category,Property,Image
from .serializers import*
from rest_framework.response import Response

from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend

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
    #adding filter support
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['id','location']
    search_fields = ['id','location']
    ordering_fields = ['id','location']
    #adding filters by id and location 
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

#implementing a search functionality maybe latelr
class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    queryset=Property.objects.all()
    serializer_class = PropertySerializer
    name='property-details'


#functionality to increment the likes


#view to handle uploading images to our folder

#si
# class  Upload(APIView):
#     def post(self,request):
#         images = request.FILES.getlist('images')
#         for image in images:
#             MultipleImage.objects.create(images=image)
#         images = MultipleImage.objects.all()
#         return Response(images, status=status.HTTP_200_OK)


class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        all_images = Image.objects.all()
        serializer = ImageSerializer(all_images, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        property = request.data['property']

        #converts querydict to original dict
        images = dict((request.data).lists())['image']

        flag=1;arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(property,img_name)
            file_serializer = ImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:flag = 0
        if flag == 1:
            return Response(arr,status=status.HTTP_201_CREATED)
        else:return Response(arr, status=status.HTTP_400_BAD_REQUEST)



#before setting as favourite we have to make sure user is subscribedto the property
class SetFav(APIView):
    def post(self, request,*args, **kwargs):
        client_name = request.data.get('name')
        property_id = request.data.get('id')

        if client_name and property_id:
            filtered_user = Client.objects.filter(name=client_name)
           
            #if filtered  what next
            filtered_property = Property.objects.filter(id=property_id)
            #first check if the user is already subscribed
            checksub = filtered_property.sub_users.filter(name__iexact=filtered_user)
            if checksub.exists():
                filtered_property.isFav = True
                return Response({
                    'status':True,
                    'detail':'property added to Favs'
                }) 
            else:
                filtered_property.sub_users = filtered_user
                filtered_property.isSub = True
                filtered_property.isFav = True  
                return Response({
                    'status':True,
                    'detail':'Property added to Favs'
                })
        else:
            return Response({
                'status':False,
                'detail':'Provide client name and property_id'
            })

class SetLike(APIView):
    def post(self,request,*args,**kwargs):
        client_name = request.data.get('name')
        property_id = request.data.get('id')

        #below checks that client name and property_id 
        if client_name and property_id:
            filtered_user = Client.objects.filter(name=client_name)
            if filtered_user.exists():
                filtered_property = Property.objects.filter(id=property_id)
                if filtered_property.exists():
                    user_property = filtered_property.sub_users.filter(name__iexact=filtered_user)
                    if user_property.exists():
                        pass
                        


#==handling setting property favourite
# class SetFav(APIView):
#     def post(self,request,*args, **kwargs):
#         username = request.data['name']#obtain the client's name
#         #filter the name against the client objects to get the specific client
#         client_sub = Client.objects.filter(name=username)
#         #after getting the details set the sub_user to the 
#         Property.objects.sub_user = client_sub 
#         Property.objects.isFav
