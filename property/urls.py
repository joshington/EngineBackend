from django.urls import path 
from .import views 

app_name = 'property'

urlpatterns = [
    path('',views.ListCategoryView.as_view(), name='categories'),
   # path('category/<int:pk>/',views.CategoryDetailView.as_view(), name="categorydetails"),
    path('category/<int:pk>/',views.CategoryProperty.as_view(), name="categoryproperties"),
    path('properties/<int:pk>/',views.PropertyDetailView.as_view(), name="propertydetails"),
    path('properties/<int:id>/<str:name>/',views.SetFav.as_view(), name="add-fav"),
]
