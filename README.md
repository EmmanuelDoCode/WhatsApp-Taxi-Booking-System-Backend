# 🚕 Taxi Dispatch Backend MVP

A Django REST Framework backend that simulates a taxi dispatch system, including ride requests, driver assignment, ride acceptance, ride rejection, automatic reassignment, and ride completion workflows.

# Overview

This project was built to practice backend software engineering concepts such as:

> REST API development

> Business logic implementation

> Workflow/state management

> Database modeling

> Driver assignment algorithms

> Error handling and validation

> Version control with Git and GitHub

The system manages the complete ride lifecycle from request creation to trip completion.

# Features

Ride Management

> Create ride requests

> Track ride status

> View ride history in Django Admin

# Driver Management:

> Register drivers

> Track driver availability

> Prevent double-booking

# Dispatch Logic:

> Automatically assign available drivers

> Prevent assignment to busy drivers

## Driver Actions:

> Accept rides

> Reject rides

> Start rides

> Complete rides

# Smart Reassignment

When a driver rejects a ride:

> The rejection is recorded

> Another available driver is searched

> The ride is reassigned automatically

If no driver is available:

> The ride is cancelled automatically

# Notifications (Console Simulation)

The system simulates customer notifications for:

> Driver assigned

> Ride accepted

> Ride started

> Ride completed

# Ride Lifecycle:

pending -> offered -> assigned -> ongoing -> completed 

# Alternative flows:

offered -> rejected -> reassigned offered -> all drivers reject -> cancelled 

# Tech Stack

• Python

• Django

• Django REST Framework

• SQLite

• Git

• GitHub

# API Endpoints

Ride Actions

|Method   |     Endpoint |
|POST     |    /api/rides/<ride_id>/accept/<driver_id>/
|POST     |     /api/rides/<ride_id>/reject/<driver_id>/
|POST     |    /api/rides/<ride_id>/start/<driver_id>/
|POST     |    /api/rides/<ride_id>/complete/<driver_id>/ 

## Project Structure:

taxi-dispatch-backend/ 
│
|--rides/
|-- api/
|-- manage.py
|-- db.sqlite3
|-- requirements.txt
|-- README.md 

## Future Improvements:

> WhatsApp integration

> Driver mobile app

> Customer mobile app

> Real-time location tracking

> Payment processing

> Ride fare calculation

> Ratings and reviews

> Driver analytics dashboard

## What I Learned:

During this project I gained practical experience with:

> Django Models

> Django Admin

> Django REST Framework

> API Design

> Business Logic Development

> Database Relationships

> Git

> GitHub

> Debugging and Error Handling

## Author:

Emmanuel Adeyemo

GitHub: https://github.com/EmmanuelDoCode
