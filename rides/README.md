Whatsapp Taxi Dispatch Backend MVP

A Django REST API backend that simulates a taxi dispatch system.

Features:

~Ride request creation

~ Driver assignment

~ Driver availability tracking

~ Ride acceptance

~ Ride rejection

~ Automatic ride reassignment

~ Ride cancellation when no drivers are available

~ Ride start and completion workflow

~ Customer notifications (console simulation)

Tech Stack:

~Python

~ Django

~ Django REST Framework

~ SQLite

Ride Lifecycle:

pending > offered > assigned > ongoing > completed

Alternative flows:

~offered > rejected > reassigned

~offered > all drivers reject > cancelled

Future Improvements:

~WhatsApp notifications

~Real-time driver location tracking

~Payment integration

~Customer mobile app

~Driver mobile app

Author: Emmanuel Adeyemo