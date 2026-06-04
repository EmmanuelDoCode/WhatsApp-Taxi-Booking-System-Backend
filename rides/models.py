from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.



class Driver(models.Model): #for driver
    name = models.CharField(max_length= 500)
    phone_number= models.CharField(max_length= 12)
    vehicle_type = models.CharField(max_length=100)
    plate_number = models.CharField(max_length= 50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    



class Ride(models.Model): #for customer

    STATUS_CHOICES = [('pending', 'Pending'),
                      ('requested', 'requested'),
                      ('offered', 'offered'),
                      ('assigned', 'Assigned'),
                      ('ongoing', 'Ongoing'),
                      ('completed', 'Completed'),
                      ('cancelled', 'Cancelled'),]

    customer_name= models.CharField(max_length= 50)
    pickup_location = models.CharField(max_length= 255)
    dropoff_location = models.CharField(max_length= 255)
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2)
    status= models.CharField(max_length=50,choices=STATUS_CHOICES, default="pending")
    driver= models.ForeignKey(Driver ,on_delete=models.SET_NULL, null= True, blank=True)
    created_at = models.DateTimeField(auto_now_add= True)


    rejected_by =     models.ManyToManyField(
    Driver,
    blank=True,
    related_name= "rejected_rides")

    accepted_by = models.ManyToManyField(
        Driver,
        blank= True,
        related_name= "accepted_rides"
    )

    def clean(self):
        if self.driver and self.status == "assigned":

            active_rides = Ride.objects.filter(
                driver = self.driver,
                status__in= ["assigned", "onging"]

            ).exclude(pk= self.pk)

            if active_rides.exists():
                raise ValidationError("This driver already has an active ride.")

    def save(self, *args, **kwargs):
        old_driver = None

        if self.pk:
            old_ride= Ride.objects.get(pk=self.pk)
            old_driver = old_ride.driver

        self.full_clean()

        # Always save
        super().save(*args, **kwargs)

    # Only run this logic if the object already enxists (update, not create)
        if self.driver:
            if self.status and self.status in ["assigned", "ongoing"]:
                self.driver.is_available= False
                self.driver.save()

            if old_driver and self.status in ["pending", "completed", "cancelled"]:
                old_driver.is_available = True

                old_driver.save()





    def __str__(self):
        return f"{self.customer_name} {self.status}"