from distutils.command.upload import upload
from locale import currency
import profile
from django.db import models
from django.forms import CharField, DateTimeField, ImageField 

class Profile(models.Model):

    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    profilepic=models.ImageField(upload_to='uploads/profile')
    location=models.TextField(max_length=300)
    about=models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Category(models.Model):

    # TODO: Define fields here
    type = models.CharField(max_length=150)
    icon =models.ImageField(upload_to='uploads/icons/')

    def __str__(self):
        return self.type

class Currency(models.Model):


    # TODO: Define fields here
    name = models.CharField(max_length=150)
    worthInD = models.DecimalField(max_digits=12,decimal_places=4)   
    
    def __str__(self):
        return self.name


class NFT(models.Model):

    # TODO: Define fields here
    title = models.CharField(max_length=150)
    createdOn=models.DateTimeField('Created On',auto_now=True)
    worthInD = models.DecimalField(max_digits=12,decimal_places=4)   
    #owner,image ,category(f),token,summary,currency(d$)
    owner=models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    image=models.ImageField(upload_to='uploads/nft')
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    token=models.TextField(max_length=500)
    summary=models.TextField(max_length=1000)
    currency=models.ForeignKey(Currency,on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.title


class bids(models.Model):

    # TODO: Define fields here
    nft=models.ForeignKey(NFT,on_delete=models.DO_NOTHING)
    #dictionary with user and their bid (top 5)
   #bidder(f),on,amount,status(acc/rej),c
    bidder=models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    bidded_on=DateTimeField()
    amountInD=models.DecimalField(max_digits=12, decimal_places=4)
    
    #accepted or rejected
    status=models.BooleanField()

    currency=models.ForeignKey(Currency,on_delete=models.DO_NOTHING)



    def __str__(self):
        return self.type




class Transaction(models.Model):
    # TODO: Define fields here
    nft=models.ForeignKey(NFT,on_delete=models.DO_NOTHING)
    buyer=models.ForeignKey(Profile,related_name='buyer' ,on_delete=models.DO_NOTHING)
    seller=models.ForeignKey(Profile,related_name='seller',on_delete=models.DO_NOTHING)
    time=models.DateTimeField()
    priceInD=models.DecimalField(max_digits=12,decimal_places=4)
    
    def __str__(self):
        return self.nft

class Follow(models.Model):
    # TODO: Define fields here
    creator=models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    #list of followers
    #noOfFollowers=len(listOfFollowers)    
    
    def __str__(self):
        return self.creator

