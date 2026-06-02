from django.contrib import admin
from .models import Ride, Driver
from django.db.models import Q
# Register your models here.


# class RideAdmin(admin.ModelAdmin):
    
    

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'vehicle_type', 'plate_number', 'is_available')
    list_filter = ('is_available', )

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "driver":
            if request.resolver_match.kwargs.get("object_id"):
                ride_id = request.resolver_match.kwargs.get("object_id")
                ride = Ride.objects.get(pk=ride_id)

                kwargs["queryset"]= Driver.objects.filter(Q(is_available= True) | Q(pk=ride.driver_id))

            else:
                kwargs["queryset"] = Driver.objects.filter(is_available= True)

        return super().formfield_for_foreignkey(db_field,request, **kwargs)

    list_display = ('customer_name', 'pickup_location', 'dropoff_location', 'estimated_price', 'status', 'created_at' )
    list_filter = ('status',)
    search_fields = ('customer_name', 'pickup_location', 'dropoff_location')



