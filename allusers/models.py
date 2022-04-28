from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save 
from django.dispatch import receiver
# Create your models here.

#models for our users of the platform
class Company(models.Model):
    company_name = models.CharField(blank=False,max_length=55,help_text='company name here')
    slug = models.SlugField(default="abc", unique=True, db_index=True)
    #since every product needs aslug generator
    email = models.EmailField(blank=False,help_text='enter company email here')
    phone_regex= RegexValidator(regex=r'^\+?1?\d{9,10}$',\
        message='phone number must be entered in the format 0706626855.upto 10digits allowed')
    phone_no = models.CharField(validators =[phone_regex], max_length=15, unique = True)
    logo = models.FileField()
    password    = models.CharField(max_length=100, null = True, blank = True, default = None)
    company_website= models.URLField(max_length=200,blank=False)

    def __str__(self):
       return self.company_name 


#now the client or the customer
class Client(models.Model):
    username = models.CharField(blank=False,max_length=55,help_text='custome name here')
    slug = models.SlugField(default="client_slug", unique=True, db_index=True)#since every product needs aslug generator
    phone_regex= RegexValidator(regex=r'^\+?1?\d{9,15}$',\
        message='phone number must be entered in the format 0706626855.upto 10digits allowed')
    phoneno  = models.CharField(validators =[phone_regex], max_length=15, unique = True)
    email =  models.EmailField(blank=False,help_text=' email here')


    def __str__(self):
        return self.username + self.email


#now our admin here
class OurAdmin(models.Model):
   username = models.CharField(blank=False,max_length=55)
   password    = models.CharField(max_length=100, null = True, blank = True, default = None) 

   def __str__(self):
       return self.username 



#target is to automatically create username for admin on creating of the object. 
#so we are gonna use a pre_save signal here

@receiver(pre_save,sender=OurAdmin)
def update_adminame(sender,instance, **kwargs):
    if instance.username is None:
        instance.username = "Marifasasa"