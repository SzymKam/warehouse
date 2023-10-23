

# WAREHOUSE

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Development Server](#running-the-development-server)
- [Usage](#usage)
- [Database](#database)
- [Testing](#testing)
- [Author](#author)


## Project Overview

This project is created to manage warehouse of medical equipment.
It is built using Django 4.1.7.
It is made especially for Medical Rescue Group of Polish Red Cross.
User can go by all containers in warehouse, create new containers
and add equipment into containers. Project includes also pre-created
list of equipment of different types of bags used in Group. 3rd part of
app is staff management.


## Features

- [Feature 1]: Containers - can manage different types of containers of list, ex. bags, trunks.
- [Feature 2]: Equipment - containers contain equipment. There is list of medical equipment to add sorted by types, ex. airways, drugs.
- [Feature 3]: Models - ready set of equipment. User can check what should be in, to make it in real.
- [Feature 4]: Staff - Diffrent groups of Staff - to manage containers and equipment or for staff management.
- [Feature 5]: Save into pdf - every list (staff, containers, equipment, equipment in container) can be downloaded in pdf version.

## Prerequisites

Ensure you have met the following requirements:

- Python 3.11
- Django 4.1.7
- PostgreSQL 15

## Getting Started

Follow these steps to get your project up and running locally.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SzymKam/warehouse
   cd src
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Configure your project by setting up environment variables:
- SECRET_KEY - default is randomly generated

Create local server of PostgreSQL, and set variables to connect:
- USER - database user
- PASSWORD - database user password
- HOST - database host
- NAME - database name

For reset user password via email, connect to email service:
- EMAIL_HOST_USER - user of email host
- EMAIL_HOST_PASSWORD - password to email host
- DEFAULT_FROM_EMAIL - email address to send mails


### Running the Development Server

1. Run database migrations:

   ```bash
   python manage.py migrate
   ```

2. Create a superuser (admin):

   ```bash
   python manage.py createsuperuser
   ```

3. Start the development server:

   ```bash
   python manage.py runserver
   ```

Your Django project should now be accessible at [http://localhost:8000/].



## Testing

To run the tests for this project, use the following command:

```bash
python manage.py test
```

For testing is used included in Django - Unit Test.
Total test coverage is 99%, with 6466 Stmts and 45 Miss.

## Author

Szymon Kamiński
https://github.com/SzymKam
