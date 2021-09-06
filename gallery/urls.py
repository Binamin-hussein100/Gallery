from django.urls import path,re_path
from . import views


urlpatterns  = [
    path('',views.images_all, name = 'the_gallery' ),
    path('search/',views.search, name='search'),
    path('details/<int:pk>/',views.details, name='picture')
    
]
