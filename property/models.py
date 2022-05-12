# //from email.policy import default
from unicodedata import category
from django.db import models
from allusers.models import*
# Create your models here.
#want to handle everything property related here
from allusers.models import*

class Category(models.Model):
    category_name = models.CharField(blank=False,max_length=55,help_text="category_name")
    cat_image = models.FileField() 


    def get_absolute_url(self):
        return Property.objects.filter(category_name=self.category_name).all()
    
    def __str__(self):
        return self.category_name



class Hotel(models.Model):
    hotel_name = models.CharField(blank=False,max_length=55,help_text='hotel  name here')
    slug = models.SlugField(default="hotel", unique=True, db_index=True)#since every product needs aslug generator
    category_name = models.ForeignKey(Category,default='0',related_name='hotel_category',on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company,related_name="company_hotel",on_delete=models.CASCADE)
    images = models.FileField()
    #question is how i add multiple images to the model
    description = models.TextField(blank=False,help_text='enter the hotel descriptions here')
    tour_link = models.URLField(blank=False) 

    def __str__(self):
        return self.hotel_name

###now for the case of the realestate what todo with it

class Apartment(models.Model):
    estate_name = models.CharField(blank=False,max_length=55,help_text='appartment name here')
    slug = models.SlugField( unique=True, db_index=True)#since every product needs aslug generator
    image = models.FileField()
    #add category to the property
    category_name = models.ForeignKey(Category,default='0',related_name='apart_category',on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company,related_name="company_apartment",on_delete=models.CASCADE)
    tour_link = models.URLField(blank=False)
    phone_regex= RegexValidator(regex=r'^\+?1?\d{9,15}$',\
        message='phone number must be entered in the format 0706626855.upto 10digits allowed')
    phone_no = models.CharField(validators =[phone_regex], max_length=15, unique = True)


    def __str__(self):
       return self.estate_name + self.company_name


#do i really need to have one single model for the property
#yah i really think i need it
class Property(models.Model):
    property_name = models.CharField(blank=False,max_length=55,help_text='property name here')
    prop_image = models.FileField()
    category_name = models.ForeignKey(Category,default='0',related_name='property_category',on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company,default='0',related_name="company_propname",on_delete=models.CASCADE)
    location = models.CharField(default='0',blank=False,max_length=55,help_text='property location')
    tour = models.URLField(blank=False,default='https://my.matterport.com/show/?m=uAAJCS3gnPF')

    sub_users  =models.ManyToManyField(Client, 
        related_name='properties_subscribed',blank=True
    )
    likes = models.PositiveIntegerField(default=0,blank=True,null=True)
    favs = models.PositiveIntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return self.property_name