from django.contrib import admin
from django.urls import path
from .views import home_page, about_page, properties_page,pro_single,contact_page,public_request

def default(req):
    return home_page()

urlpatterns = [
    path('home/', view= home_page ,name='home'),
    path('about/', view= about_page ,name='about'),
    path('properties/', view= properties_page ,name='properties'),
    path('contact/', view= contact_page ,name='contact'),
    path('public_request/', view= public_request ,name='public_request'),
    path('prop-single/<int:id>', view= pro_single ,name='propsingle'),
    path('', view= home_page),
]
