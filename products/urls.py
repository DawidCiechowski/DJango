from django.urls import path
from . import views

# /products
# /products/1/details
# /products/new

#Set the redirects paths
#Trolololo
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]