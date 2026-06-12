# User Management API

## Overview

This project is a RESTful User Management API built using Django, Django REST Framework, and MySQL. The API provides functionality for creating, retrieving, searching, and managing users. JWT authentication has been implemented to secure the endpoints.

---

# Tech Stack

* Python
* Django
* Django REST Framework (DRF)
* MySQL
* JWT Authentication (Simple JWT)

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone <repository-url>
cd user_management_api
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure MySQL Database

Create a database named:

```sql
CREATE DATABASE users;
```

Update the database configuration in `settings.py`.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'users',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 6. Create Superuser

```bash
python manage.py createsuperuser
```

## 7. Run Server

```bash
python manage.py runserver
```

Server URL:

```text
http://127.0.0.1:8000/
```

---

# Authentication

JWT Authentication is used.

## Obtain Access Token

### Request

```http
POST /api/token/
```

```json
{
    "username": "admin",
    "password": "password"
}
```

### Response

```json
{
    "refresh": "refresh_token",
    "access": "access_token"
}
```

## Use Access Token

Add the following header:

```text
Authorization: Bearer <access_token>
```

---

# API Endpoints

## 1. Get All Users

### Request

```http
GET /api/users/
```

### Response

```json
{
    "success": true,
    "count": 2,
    "data": [
        {
            "id": 1,
            "name": "Ajit",
            "email": "ajit@gmail.com",
            "role": "Developer"
        }
    ]
}
```

---

## 2. Create User

### Request

```http
POST /api/users/
```

```json
{
    "name": "Ajit",
    "email": "ajit@gmail.com",
    "role": "Developer"
}
```

### Response

```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "Ajit",
        "email": "ajit@gmail.com",
        "role": "Developer"
    }
}
```

---

## 3. Get User By ID

### Request

```http
GET /api/users/1/
```

### Response

```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "Ajit",
        "email": "ajit@gmail.com",
        "role": "Developer"
    }
}
```

### User Not Found Response

```json
{
    "success": false,
    "error": "User not found"
}
```

---

## 4. Search Users

### Request

```http
GET /api/users/?search=ajit
```

### Response

```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "Ajit",
            "email": "ajit@gmail.com",
            "role": "Developer"
        }
    ]
}
```

---

## 5. Pagination

### Request

```http
GET /api/users/?page=1&limit=10
```

### Response

```json
{
    "success": true,
    "count": 25,
    "total_pages": 3,
    "current_page": 1,
    "data": [...]
}
```

---

# Validation & Error Handling

## Required Fields

* name
* email
* role

### Response

```json
{
    "success": false,
    "errors": {
        "email": [
            "This field is required."
        ]
    }
}
```

## Invalid Email Format

```json
{
    "success": false,
    "errors": {
        "email": [
            "Enter a valid email address."
        ]
    }
}
```

## Duplicate Email

```json
{
    "success": false,
    "errors": {
        "email": [
            "Email already exists"
        ]
    }
}
```

---

# Database Schema

Database Name:

```text
users
```

Table:

```text
users_user
```

| Column | Type         | Constraints |
| ------ | ------------ | ----------- |
| id     | Integer      | Primary Key |
| name   | VARCHAR(100) | Not Null    |
| email  | VARCHAR(254) | Unique      |
| role   | VARCHAR(50)  | Not Null    |

---

# Assumptions Made

1. Email addresses must be unique for each user.
2. JWT authentication is required to access user management endpoints.
3. Pagination defaults to page=1 and limit=10 when not provided.
4. Search functionality supports searching by name and email.
5. The API is JSON-based and does not provide HTML responses.
6. Django's built-in authentication system is used for JWT login.
7. MySQL is used as the primary database.

---

# AI Usage Declaration

## AI Tools Used

* ChatGPT

## AI Generated Assistance

* Project structure suggestions
* README documentation template


## Manual Modifications

* Implemented Django models
* Implemented API views and serializers
* Added pagination
* Added validation and error handling
* Configured JWT authentication
* Tested API endpoints and database integration
