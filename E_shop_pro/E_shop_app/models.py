from typing import OrderedDict
from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
class Userreg(models.Model):
    username = models.CharField(max_length=200,null=True,blank=False)
    password = models.CharField(max_length=200,null=True,blank=False)
    comfirm_password = models.CharField(max_length=200,null=True,blank=False) 
    your_email = models.CharField(max_length=200,null=True,blank=False)

class Brand(models.Model):
    bname=models.CharField(max_length=200,null=True,blank=False)
    bdes=models.TextField(max_length=500,null=True,blank=False)
    img=models.ImageField(upload_to='image',null=True,blank=False)    

class brandladies(models.Model):
    fname=models.CharField(max_length=200,null=True,blank=False)
    description=models.CharField(max_length=200,null=True,blank=False)
    img=models.ImageField(upload_to='image',null=True,blank=False)    


class scdb(models.Model):
    name=models.CharField(max_length=25,null=True,blank=False)
    description=models.CharField(max_length=200,null=True,blank=False)
    img=models.ImageField(upload_to='image',null=True,blank=False)  

class Product(models.Model):
    pname=models.CharField(max_length=200,null=True,blank=False)
    brname=models.CharField(max_length=200,null=True,blank=False)
    pdes=models.TextField(max_length=200,null=True,blank=False)
    price=models.IntegerField(null=True,blank=False)
    discount=models.IntegerField(null=True,blank=False)
    color=models.CharField(max_length=200,null=True,blank=False)
    size=models.CharField(max_length=200,null=True,blank=False)
    pimg=models.ImageField(upload_to='image',null=True,blank=False)


class lpro_db(models.Model):
    product_name=models.CharField(max_length=200,null=True,blank=False)
    categorie=models.CharField(max_length=200,null=True,blank=False)
    product_description=models.CharField(max_length=200,null=True,blank=False)
    price=models.IntegerField(null=True,blank=False)
    discount=models.IntegerField(null=True,blank=False)
    color=models.CharField(max_length=200,null=True,blank=False)
    size=models.CharField(max_length=200,null=True,blank=False)
    img=models.ImageField(upload_to='image',null=True,blank=False)

class pdb(models.Model):
    pname=models.CharField(max_length=25,null=True,blank=False)
    category=models.CharField(max_length=25,null=True,blank=False)
    pdescription=models.CharField(max_length=200,null=True,blank=False)
    color=models.CharField(max_length=200,null=True,blank=False)
    price=models.IntegerField(null=True,blank=False)
    discount=models.IntegerField(null=True,blank=False)
    size=models.CharField(max_length=25,null=True,blank=False)
    file2=models.ImageField(upload_to='picture/',null=True,blank=False)

class shopCart(models.Model):
    Kproductid = models.ForeignKey(pdb,on_delete=CASCADE,null=True,blank=True)
    Gproductid = models.ForeignKey(Product,on_delete=CASCADE,null=True,blank=True)
    Lproductid = models.ForeignKey(lpro_db,on_delete=CASCADE,null=True,blank=True)
    userid = models.ForeignKey(Userreg,on_delete=CASCADE,null=True,blank=False)
    total = models.IntegerField(null=True,blank=False)
    quantity = models.IntegerField(null=True,blank=False)
    status = models.IntegerField(null=True,blank=False)    

class ShopCheckout(models.Model):
    cartid = models.ForeignKey(shopCart,on_delete=CASCADE,null=True,blank=False)
    fname = models.CharField(max_length=200,null=True,blank=False)
    lname=models.CharField(max_length=200,null=True,blank=False)
    email = models.EmailField(null=True,blank=False)
    address1 = models.TextField(max_length=200,null=True,blank=False)
    c_name = models.CharField(max_length=200,null=True,blank=False) 
    order_place = models.CharField(max_length=200,null=True,blank=False) 
    number = models.IntegerField(null=True,blank=False)
    post = models.IntegerField(null=True,blank=False) 
    address2 = models.TextField(max_length=200,null=True,blank=False)

class Review_Analysis(models.Model):
    clothingid=models.CharField(max_length=200,null=True,blank=False)
    age=models.CharField(max_length=200,null=True,blank=False)
    reviewtext=models.TextField(max_length=200,null=True,blank=False)
    rating=models.IntegerField(null=True,blank=False)
    Recommended=models.IntegerField(null=True,blank=False)
    Positive=models.CharField(max_length=200,null=True,blank=False)
    Division_Name=models.CharField(max_length=200,null=True,blank=False)
    Department_Name=models.ImageField(upload_to='image',null=True,blank=False)

class Review(models.Model):
    name=models.CharField(max_length=200,null=True,blank=False)
    email=models.TextField(max_length=500,null=True,blank=False)
    re=models.CharField(max_length=200,null=True,blank=False)
