# API Planetarium Service

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

**Admin Credentials:**

  - *Email: admin_@gmail.com*
  - *Password: 54321*

## Getting Started
### Prerequisites
Before you begin, make sure you have the following tools and technologies installed:

- Python (>=3.6)
- Django
- Django REST framework

### Installing using GitHub
1. Open Terminal and open folder to clone project in.

2. Clone repository into a desirable folder:
```bash
git clone https://github.com/sakhaline/planetarium-api-service.git
```
3. Open cloned folder in terminal.
4. If you don't have pip installed [install it here](https://pip.pypa.io/en/stable/installation/#).
5. Create and activate **Virtual environment**:

**Windows**
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
**MacOS or Linux**
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
6. Open cloned folder and install needed requirements using:
```bash
pip install -r requirements.txt
```
7. Migrate:
```bash
python manage.py migrate
```
8. Install database fixture:
```bash
python manage.py loaddata db_data.json
```
9. Create .env file using *env_example* file
10. Run server:
```bash
python manage.py runserver
```
11. Go to http://127.0.0.1:8000/
### Run with Docker
Docker should be installed.
```bash
docker-compose build
docker-compose up
```
### Getting access:
- create user via api/user/register
- get access token via api/user/token
## Schema
![Screenshot from 2023-12-13 06-43-24.png](..%2F..%2F..%2F..%2FPictures%2FScreenshots%2FScreenshot%20from%202023-12-13%2006-43-24.png)
## Swagger Documentation
![Screenshot from 2023-12-13 07-35-51.png](..%2F..%2F..%2F..%2FPictures%2FScreenshots%2FScreenshot%20from%202023-12-13%2007-35-51.png)