from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path("",home,name='home'),
    path("about/",about,name='about'),
    path("services/",services,name='services'),
    path("home/",emp_home,name='emphome'),
    path("add-emp/",add_emp,name='add'),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
]