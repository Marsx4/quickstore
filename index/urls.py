from django.urls import path
from .views import site_home_view,about,contact,terms

urlpatterns=[
    path('',site_home_view,name='site_home'),
    path('about/',about,name='site_about'),
    path('contact/',contact,name='site_contact'),
    path('terms/',terms,name='site_terms'),
]