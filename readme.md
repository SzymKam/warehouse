
```markdown
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
- [Feature 3]: Save into pdf - every list (staff, containers, equipment, equipment in container) can be downloaded in pdf version.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.11
- Django 4.1.7
- PostgreSQL[Any other dependencies or libraries]
- [Database system and its configuration]



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
```
