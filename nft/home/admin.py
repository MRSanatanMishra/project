from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ('name','email','location','about')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('type',)

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    '''Admin View for Currency'''

    list_display = ('name','worthInD')

@admin.register(NFT)
class NFTAdmin(admin.ModelAdmin):
    '''Admin View for NFT'''

    list_display = ('title','createdOn','worthInD','owner',
                    'category','token','currency')
  
@admin.register(bids)
class bidsAdmin(admin.ModelAdmin):
    '''Admin View for bids'''

    list_display = ('nft','bidder','bidded_on','amountInD','status','currency')

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    '''Admin View for Follow'''

    list_display = ('creator',)
    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    '''Admin View for Transaction'''

    list_display = ('nft','buyer','seller','time','priceInD')


    