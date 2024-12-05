# Reporting Service
## Overview
The Reporting Service is a core microservice in the Wildlife Sighting Management System. It allows users to report wildlife sightings, including geolocation, descriptions, and multimedia evidence. The service provides APIs for creating, retrieving, filtering, and sorting reports and integrates with other services for notifications and management.

## Features
1. **Anonymous Reporting**: Users can submit reports without authentication.
2. **Rich Input**: Accepts animal type, description, location, and photo uploads.
3. **Filtering and Sorting**: APIs support dynamic queries on status, type, and creation date.
4. **Scalability**: Designed to handle high report volumes with efficient queries.
5. **API Documentation**: DRF Spectacular provides a user-friendly API schema.










1. Change docker cmd command to use gunicorn in production
2. change docker compose to also use gunicorn in production