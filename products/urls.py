from django.urls import path
from . import views

# /products
# /products/1/details
# /products/new

#Set the redirects paths
#Trolololo
#Hey ho, hey ho
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]