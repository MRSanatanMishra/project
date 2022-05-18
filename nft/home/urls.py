"""nft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.views.generic import TemplateView

from home.views import nft_create
urlpatterns = [

    path('',TemplateView.as_view(template_name='index-3.html')),
    path('index',TemplateView.as_view(template_name='index-3.html')),
    path('index-2',TemplateView.as_view(template_name='index-2.html')),
    path('index-3',TemplateView.as_view(template_name='index.html')),
    
    path('blog',TemplateView.as_view(template_name='blog.html')),
    path('blog-2',TemplateView.as_view(template_name='blog-2.html')),
    path('blog-3',TemplateView.as_view(template_name='blog-3.html')),

    path('blog-single',TemplateView.as_view(template_name='blog-single.html')),
    path('blog-single-2',TemplateView.as_view(template_name='blog-single-2.html')),


    path('contact',TemplateView.as_view(template_name='contact.html')),
    path('explore',TemplateView.as_view(template_name='explore.html')),
    path('item-details',TemplateView.as_view(template_name='item-details.html')),
    path('signin',TemplateView.as_view(template_name='signin.html')),
    path('signup',TemplateView.as_view(template_name='signup.html')),
    path('wallet',TemplateView.as_view(template_name='wallet.html')),
    path('author',TemplateView.as_view(template_name='author.html')),
    path('author',TemplateView.as_view(template_name='author.html')),
    path('auction',TemplateView.as_view(template_name='auction.html')),
    path('all-authors',TemplateView.as_view(template_name='all-authors-2.html')),
    path('all-authors-2',TemplateView.as_view(template_name='all-authors.html')),
    path('activity',TemplateView.as_view(template_name='activity.html')),
    path('404',TemplateView.as_view(template_name='404.html')),
    path('forgot-pass',TemplateView.as_view(template_name='forgot-pass.html')),
    path('coming-soon',TemplateView.as_view(template_name='coming-soon.html')),
    

    path('create',nft_create,name='create')

]
