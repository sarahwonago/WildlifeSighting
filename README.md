# WildlifeSightingAPI
## Overview
The Wildlife Sighting Management System is a microservices-based platform that facilitates the reporting, notification, and management of wildlife sightings in urban areas. The system consists of three interconnected services:

- **Reporting Service**: Allows users to report wildlife sightings.
- **Notification Service**: Alerts communities in real-time about wildlife sightings in their area.
- **Authority Management Service**: Enables authorities to review, manage, and resolve reports.

This project is designed with scalability, performance, and maintainability in mind and adheres to production-ready best practices.

## Features
1. Wildlife Reporting: Anonymous users can report wildlife sightings, including geolocation, description, and images.
2. Real-Time Notifications: Alerts sent to communities about nearby wildlife activity.
3. Authority Dashboard: Provides tools for authorities to manage reports and track resolutions.
4. Secure Inter-Service Communication: JWT-based authentication ensures secure data sharing.
5. Microservices Architecture: Separation of responsibilities across independently deployable services.
6. Geospatial Queries: Supports location-based filtering using PostGIS.


## Architecture
The project uses a microservices architecture with the following stack:

**Backend**
Python/Django: Main framework for the services.
Django REST Framework (DRF): API development.
PostgreSQL with PostGIS: Relational database with geospatial capabilities.
Celery with RabbitMQ: Asynchronous task queue for notifications.
Redis: Caching

**Frontend**
React.js: For web dashboard and community interface.

**Infrastructure**
Docker: Containerized deployment.
Kubernetes: Orchestration for microservices.
Prometheus and Grafana: Monitoring and observability.

Service Breakdown
1. **Reporting Service**
Accepts wildlife reports.
Validates inputs such as geolocation, description, and multimedia.
Provides RESTful APIs for report creation, retrieval, filtering, and sorting.
2. **Notification Service**
Consumes wildlife sighting reports from the Reporting Service.
Sends notifications to subscribed users or communities in the affected area.
Uses WebSockets for real-time alerts.
3.**Authority Management Service**
Fetches and manages reports from the Reporting Service via inter-service API communication.
Allows status updates and prioritization of reports.
Provides analytics and trends for wildlife sightings.
