from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
PURPOSE_CHOICES = (
    ('rent','rent'),
    ('sell','sell'),
)

class Property(models.Model):
    name = models.CharField(max_length=100)
    prop_type = models.CharField(max_length=6, choices=PURPOSE_CHOICES, default='rent')
    photo = models.ImageField(upload_to="pro-img/")
    price = models.FloatField()
    desc = models.TextField(max_length=500)
    location = models.TextField(max_length=300)
    status = models.BooleanField(default=True)
    area = models.FloatField(default=0)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)

    def image_tag(self): # new
        return mark_safe (
            '''<a href="/../../media/%s" >
                  <img src="/../../media/%s" width="90" height="90" />
               </a>
            ''' % (self.photo,self.photo))
    
class Agent(models.Model):
    name =  models.CharField(max_length=100)
    photo = models.ImageField(upload_to="agent-img/")
    phone_no = models.CharField(max_length=10)
    email = models.EmailField(max_length = 254,null= False, blank = False)
    desc = models.TextField(max_length=500)

    def image_tag(self): # new
        return mark_safe (
            '''<a href="/../../media/%s" >
                  <img src="/../../media/%s" width="90" height="90" />
               </a>
            ''' % (self.photo,self.photo))
class pub_mail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254,null= False, blank = False)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    

