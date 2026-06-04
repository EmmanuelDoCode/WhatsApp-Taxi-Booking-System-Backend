from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from  rest_framework.response  import Response
from .models import Ride, Driver
from .serializers import RideSerializer
import requests


@api_view(["POST"])
def reject_ride(request, ride_id, driver_id):
    try:
        ride = Ride.objects.get(id = ride_id)
        driver= Driver.objects.get(id = driver_id)
        
    except Ride.DoesNotExist:
        return Response({"error": "Ride not found"}, status= 404)
    
    except Driver.DoesNotExist:
        return Response({"error": "Driver not found"}, status= 404)
    
    # this record rejection
    ride.rejected_by.add(driver)

    # this find another available driver
    next_driver = Driver.objects.filter(is_available = True).exclude(id__in= ride.rejected_by.values_list("id", flat=True)).first()

    if next_driver:
        ride.driver = next_driver
        ride.status = "offered"
        ride.save()

        return Response({
            "message": f"Ride offered to {next_driver.name}"
                        })
    
    # no driverr left?
    ride.driver = None
    ride.status = "cancelled"
    ride.save()

    return Response({"message": "No driver is available. Ride cancelled"})


@api_view(["POST"]) #this works whatsapp request
def whatsapp_webhook(request):
    data = request.data

    available_driver = Driver.objects.filter(is_available = True).first()#this auto add drive to ride

    ride = Ride.objects.create(
        customer_name =data["customer_name"],
        pickup_location = data["pickup_location"],
        dropoff_location = data["dropoff_location"],
        estimated_price = 5000,
        driver = available_driver,
        status = "assigned" if  available_driver else "pending" #this assign driver if is available
    )
    if available_driver:
        print("\n=== CUSTOMER NOTIFICATION ===")
        print(
            f"Hello {ride.customer_name},"
            f"your ride has been assigned. \n"
            f"Driver: {available_driver.name}\n"
            f"Vehicle: {available_driver.vehicle_type}\n"
            f"plate Number: {available_driver.plate_number}"
        )
        print("================================")

    

    return Response({"message": "Ride created",
                     "ride_id": ride.id})


# PHONE_NUMBER_ID = "09133589360"
# ACCESS_TOKEN = "MY TOKEN"

# def send_whatsapp_message(to, message):
#     """sends a text message to a whatsapp number"""
    
#     url = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/ messages"
#     headers = {"Authorization": f"Bearer{ACCESS_TOKEN}", "Content-Type": "application/json"}
#     data = {"messaging_product": "whatsapp", "to": to, "type": "text", "text": {"body": message}}

#     response = requests.post(url, headers=headers, json= data)
#     return requests.json()

@api_view(['POST'])
def driver_response(request, ride_id):

    action = request.data.get("action")
    driver_id= request.data.get("driver_id")

    try:
        ride = Ride.objects.get(id= ride_id)
        driver = Driver.objects.get(id = driver_id)
    
    except Ride.DoesNotExist:
        return Response({"error": "Ride not found"}, status=404)
    except Driver.DoesNotExist:
        return Response({"error": "Driver not found"}, status= 404)
    

    # to accept ride
    if action == "accept":
        if not driver.is_available:
            return Response({"error": "Driver is not available"}, status=400)
        ride.driver=driver
        ride.status= "assigned"
        ride.save()
        return Response({"message": f"{driver.name} accept the ride"})
    

    # to reject
    elif action == "reject":
        return Response({"message": f"{driver.name}rejected the ride"})
    
    return Response({"error": "invalid action"}, status= 400)



# @api_view(['POST'])
# def ride_from_whatsapp(request):
#     """Accept ride requests from webhook simulation
#        JSON example:
#        {
#         "customer_name"= "Adeyemo"
#         "pick_up": = "ikeja"
#         "drop_off: = "london"
#        }
#     """
#     data = request.data
#     customer_name  = data.get('customer_name')
#     pickup = data.get('pickup')
#     dropoff = data.get('dropoff')

#     if not all(['customer_name', 'pickup', 'dropoff']):
#         return Response({"error": "Missing data"}, status= 400)
    
#     estimated_price = 1000

#     ride = Ride.objects.create(customer_name= customer_name,
#                                pickup_location = pickup,
#                                dropoff_location = dropoff,
#                                estimated_price = estimated_price)
#     reply = f"Hi {customer_name.upper()}, your ride from {pickup} to {dropoff} has been received.\n Estimated fare: #{estimated_price}. \n we will assign a driver shortly."
#     print(reply)
    
#     serializer = RideSerializer(ride)
#     return Response(serializer.data, status= 201) 




@api_view(['GET', 'POST'])
def ride_list_create(request):
    if request.method == 'GET':
        rides = Ride.objects.all()
        serializer = RideSerializer(rides, many =True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer= RideSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status=400)
