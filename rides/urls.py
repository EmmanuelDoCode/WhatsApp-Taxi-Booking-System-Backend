from django.urls import path
from . import views
from .views import driver_response
from .views import whatsapp_webhook
from .views import reject_ride, accept_ride, start_ride, complete_ride

urlpatterns =[ path('rides/', views.ride_list_create, 
                                        name= 'ride_list_create'),
                        #        path('rides/whatsapp/', views.ride_from_whatsapp, name= 'ride_from_whatsapp'),
                                path('rides/<int:ride_id>/driver-response/', driver_response, name = 'driver_response'),
                                path("webhook/", whatsapp_webhook),
                                path("rides/<int:ride_id>/reject/<int:driver_id>/", reject_ride, name="reject_ride"),
                                path("rides/<int:ride_id>/accept/<int:driver_id>/", accept_ride, name="accept_ride"),
                                path("rides/<int:ride_id>/start/<int:driver_id>/", start_ride, name="start_ride"),
                                path("rides/<int:ride_id>/complete/<int:driver_id>/", complete_ride, name="complete_ride"),


                   
                   ]  