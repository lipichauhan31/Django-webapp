# Django User and Customer Management Website

## Project Overview

This project is a web application developed using **Python and Django**. It contains a website frontend and two custom Django database models: `User` and `Customer`.

The project demonstrates Django's Model-View-Template (MVT) architecture, database management, and integration with the Django Administration Panel.

## Features

- Django-based web application.
- Two custom database models: User and Customer.
- User management with name and email fields.
- Customer management with name and phone number fields.
- Django Admin Panel for managing user and customer records.
- SQLite database integration.
- Multiple website pages:
  - Home
  - About
  - Company
  - Contact
  - Design
  - News
- HTML templates with CSS, JavaScript, and image assets.

## Models

### 1. User Model

The User model stores user information.

| Field | Data Type | Description |
|---|---|---|
| id | BigAutoField | Primary key (automatically generated) |
| name | CharField | User's name (maximum 50 characters) |
| email | EmailField | User's email address (unique) |

### 2. Customer Model

The Customer model stores customer information.

| Field | Data Type | Description |
|---|---|---|
| id | BigAutoField | Primary key (automatically generated) |
| name | CharField | Customer's name (maximum 50 characters) |
| number | CharField | Customer's phone number (maximum 10 characters) |

Both models are registered in the Django Admin Panel, where records can be managed.

## Technologies Used

- Python
- Django 5.1.7
- SQLite3
- HTML
- CSS
- JavaScript
- Bootstrap

## Project Structure

```text
P3/
└── website/
    ├── app/
    │   ├── migrations/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    │
    ├── website/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── views.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── templates/
    ├── static/
    └── manage.py
```

## Installation and Setup

### 1. Install Django

```bash
pip install Django==5.1.7
```

### 2. Apply Migrations

```bash
python manage.py migrate
```

### 3. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the instructions to create your admin credentials.

### 4. Run the Development Server

```bash
python manage.py runserver
```

Open the following URL in your browser:

http://127.0.0.1:8000/

To access the Django Admin Panel:

http://127.0.0.1:8000/admin/

## Database Management

The project uses SQLite as its default database.

The two custom models, `User` and `Customer`, are defined in:

```text
app/models.py
```

Their administration configurations are defined in:

```text
app/admin.py
```

## Future Improvements

- Add user and customer registration forms.
- Implement CRUD operations (Create, Read, Update, Delete).
- Add form validation.
- Improve authentication and authorization.
- Integrate a more advanced database if required.

## License

This project is available for educational and learning purposes.
