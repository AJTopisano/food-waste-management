from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User

# Create your models here.

class fdcategory(models.Model):
    name = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    

    def __str__(self):
        return self.name

class fpost(models.Model):
    category = models.ForeignKey("fdcategory",on_delete=SET_NULL,null=True)
    name = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=500,null=True)
    phone= models.CharField(max_length=500,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
   # author = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    authname = models.CharField(max_length=500,null=True)
    location = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name


