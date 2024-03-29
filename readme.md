# WAREHOUSE

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Usage](#usage)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Run in Docker](#run-in-docker)
  - [Running the Development Server](#running-the-development-server)
- [Database](#database)
- [Testing](#testing)
- [Author](#author)

## Project Overview

This project is created to manage warehouse of medical equipment.
It is built using Django 5.0.2.
It is made especially for Medical Rescue Group of Polish Red Cross.
User can go by all containers in warehouse, create new containers
and add equipment into containers. Project includes also pre-created
list of equipment of different types of bags used in Group. 3rd part of
app is staff management.
All Create, Read, Update, Delete operations on models are available via API.

Project is available on AWS cloud service EB EC2 supported by S3 bucket for static and media files;
RDS for PostgeSQL database:

#### URL: http://warehouse.eu-north-1.elasticbeanstalk.com/

#### Demo account access:

- Login: "DemoAccount"
- Password: "43cPVy6CLZbKUjv"

## Technologies:

The most important technologies used in the project:

- Python 3.11
- Django 4.2.7
- DjangoRestFramework 3.14.0
- Poetry 1.7.1
- AWS: EB, EC2, S3, RDS
- PostgreSQL 16
- Docker 24.0.5
- Nginx 1.25
- Pre-commit 3.6.2
- Xhtml2pdf 0.2.15
- Crispy-bootstrap4 2022.1

## Usage

To enter into service you need to have user account. It's for safety reasons - information about some equipment and
calendar access may be sensitive. In main page you have menu and information about Group calendar, links into social media (FB, Instagram).

#### Main page

![Main page](docs/readme_images/main_page.jpg)
Main page - only users logged into Google account with permissions to calendar can see it.

<details>
<summary>Containers</summary>

![Container page_1](docs/readme_images/containers_view_1.jpg)
Container list. From this page user can create new container, add equipment or downlnoad pdf list of containers.

![Container page_2](docs/readme_images/containers_view_2.jpg)
Creating new container. User can choose name form list and add own description.

</details>

<details>
<summary>Equipment</summary>

![Equipment page_1](docs/readme_images/equipment_1.jpg)
Add new equipment from list

![Equipment page_2](docs/readme_images/equipment_2.jpg)
![Equipment page_3](docs/readme_images/equipment_3.jpg)
Depends on name of equipment, creates different model - with specific fields.

![Equipment page_4](docs/readme_images/equipment_4.jpg)
List of equipment from container. User can manage equipment and download equipment list of container.

![Equipment page_5](docs/readme_images/equipment_5.jpg)
It's possible to get all equipment of all containers together.

</details>

<details>
<summary>Equipment - pdf doc</summary>

![Equipment page_6](docs/readme_images/pdf.jpg)
List of all equipment in pdf.

</details>

<details>
<summary>API</summary>
![Api_1](readme_images/api_1.jpg)
Example of API response of at "/api/containers/"

![Api_2](docs/readme_images/api_2.jpg)
Example of API response of at "/api/equipment/"

</details>

## Features

- [Feature 1]: Containers - can manage different types of containers of list, ex. bags, trunks.
- [Feature 2]: Equipment - containers contain equipment. There is list of medical equipment to add sorted by types, ex. airways, drugs.
- [Feature 3]: Models - ready set of equipment. User can check what should be in, to make it in real.
- [Feature 4]: Staff - Different groups of Staff - to manage containers and equipment or for staff management.
- [Feature 5]: Save into pdf - every list (staff, containers, equipment, equipment in container) can be downloaded in pdf version.
- [Feature 6]: API - CRUD operations on models are available via API.

## Getting Started

Follow these steps to get your project up and running locally.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SzymKam/warehouse
   ```

2. Create a virtual environment and install poetry (optional but recommended):

   ```bash
    pip install poetry
    poetry env use python3.11
   ```

3. Install project dependencies:

   ```bash
    poetry install
   ```

### Configuration

Configure your project by setting up environment variables:

- SECRET_KEY - default is randomly generated

Create local server of PostgreSQL, and set variables to connect:

- DB_USER - database user
- DB_PASSWORD - database user password
- DB_HOST - database host
- DB_NAME - database name

For reset user password via email, connect to email service:

- EMAIL_HOST_USER - user of email host
- EMAIL_HOST_PASSWORD - password to email host
- DEFAULT_FROM_EMAIL - email address to send mails

If you want to connect project with your AWS S3 bucket or RDS database project is prepared.

S3 bucket settings:

- USE_RDS - set 'True' if you want to use RDS in project
- RDS_DB_NAME - your RDS name
- RDS_USERNAME - your RDS username
- RDS_PASSWORD - your RDS password
- RDS_HOSTNAME - your RDS host

AWS S3 configuration

- USE_S3 - set 'True' if you want to use S3 for static and media files in project
- AWS_ACCESS_KEY_ID - your AWS access key id
- AWS_SECRET_ACCESS_KEY - your AWS secret access key
- AWS_STORAGE_BUCKET_NAME - your S3 bucket name

To help set local variables correctly, you can use ".env.dist" file. Copy this file as ".env" and set you variables values.

### Running the Development Server

1. Run database migrations:

   ```bash
   cd src
   poetry run python manage.py migrate
   ```

2. Create a superuser (admin):

   ```bash
   poetry run python manage.py createsuperuser
   ```

3. Start the development server:

   ```bash
   poetry run python manage.py runserver
   ```

Your Django project should now be accessible at [http://localhost:8000/].

### Run in Docker

Project includes pre-made files to run 3 docker containers: web app, database (PostgreSQL) and Nginx for staticfiles.
Make sure you have installed and running Docker engine. To run project:

```bash
docker compose up --build
```

Your Django project should now be accessible at [http://localhost/].
Don't forget to make migrations, collect static files and createsuperuser.

```bash
docker-compose  exec web python manage.py migrate (migrations are also included, when docker-compose run)
docker-compose  exec web python manage.py collectstatic
docker-compose  exec web python manage.py createsuperuser
```

## Database

Overview of the database structure and models:

- [Model 1]: Container - with fields: name and description. Default container is "Main warehouse" -
  auto-created when database migrate. Also, when delete other container, equipment is transferred into
  "Main warehouse".
- [Model 2]: StaffUser - inherits from Django AbstractUser. Add additional fields (position, medical_qualifications, qualifications_expiration_date, image).
  This model is used as default AuthUserModel.
- [Model 3]: BaseMedicalEquipment - base for medical equipment. It's not used separately. Other models inherit from it:
  Drug, MedicalEquipment, Fluid, Cannula, Needle, Syringe, BIG, LtTube, Gloves, SterileGloves, Gauze, NasopharyngealTube,
  OropharyngealTube, EndotrachealTube, LaryngoscopeBlade, OxygenMask, VentilationMask - each of them with specific fields.

## Testing

To run the tests for this project, use the following command:

```bash
poetry run python manage.py test
```

For testing is used included in Django - Unit Test.
Total test coverage is 99%, with 6466 Stmts and 45 Miss.

## Author

SzymKam

https://github.com/SzymKam
