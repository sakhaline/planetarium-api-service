# PlanetariumService API

The API Planetarium Service is a comprehensive platform that enables the management and orchestration of a virtual planetarium experience, facilitating astronomy shows, reservations, and ticketing within a simulated planetarium dome. The service is designed to provide a seamless and immersive experience for both administrators and users interested in exploring the wonders of the cosmos.

## Key Components
### Show Theme:

Categorize and organize astronomy shows based on different topics and subjects.
### Planetarium Dome:

Virtual spaces where astronomy shows are hosted, each with a specific name, seating arrangement, and capacity.
### Astronomy Show:

Create and manage astronomy shows with titles, descriptions, and associated themes.
### Reservation:

Secure seats for upcoming astronomy shows with user-specific reservations.
### Show Session:

Instances of astronomy shows within a particular Planetarium Dome, including details on the associated show, hosting dome, and scheduled time.
### Ticket:

Reserve specific seats for a show with detailed information on seat location, show session association, and reservation details.

### User:
Custom user model for authentication, extending the AbstractUser model.

# Getting Started
### Prerequisites
Before you begin, make sure you have the following tools and technologies installed:

- Python (>=3.6)
- Docker
- Docker Compose

### Installing using GitHub
1. Open Terminal and open folder to clone project in.

2. Clone repository into a desirable folder:
```bash
git clone https://github.com/sakhaline/planetarium-api-service.git
```
3. You can open project in IDE and configure .env file using .env.sample file 
as an example.
4. Build and run the Docker containers:
```bash
docker-compose up --build
```
The API will be accessible at http://localhost:8000/.
### Getting access:
- create user via api/user/register
- get access token via api/user/token
## Schema
![Screenshot from 2023-12-13 06-43-24](https://github.com/sakhaline/planetarium-api-service/assets/130174413/f856ff4f-b364-4c7c-a8bb-95c525ddf837)
## Swagger Documentation
![Screenshot from 2023-12-13 07-35-51](https://github.com/sakhaline/planetarium-api-service/assets/130174413/33be0f3b-de3c-43f1-ba3d-2d16ae6026f4)
