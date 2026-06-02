from django.urls import path
from . import views
from .views import driver_response
from .views import whatsapp_webhook

urlpatterns =[ path('rides/', views.ride_list_create, 
                                        name= 'ride_list_create'),
                        #        path('rides/whatsapp/', views.ride_from_whatsapp, name= 'ride_from_whatsapp'),
                                path('rides/<int:ride_id>/driver-response/', driver_response, name = 'driver_response'),
                                path("webhook/", whatsapp_webhook),
                                
                                
                   
                   ]  