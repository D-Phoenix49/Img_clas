from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path("imghome/",index,name='imghome'),
    path("imghome/predictImage",predictImage, name ='predictIamge'),
    path("viewDataBase",viewDataBase, name ='viewDataBase'),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    
