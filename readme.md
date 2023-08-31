
# Student Management System

![PyPI - Python Version](https://img.shields.io/badge/python-3.10-blue
)

This project aims to create an API using Django and Django Rest Framework. It includes Student, Course, and Grade models, supporting CRUD operations and an authentication mechanism.








## Installation

Follow these steps to set up the project:

1- Install Virtual Environment First
```bash
$  pip install virtualenv
```
2- Create Virtual Environment
```bash
$  python3 -m venv venv
```
3- Activate Virtual Environment
```bash
$  source venv/bin/activate
```
## Run Locally

Clone the project

```bash
  git clone https://github.com/eaarda/student-management-system.git
```

Go to the project directory

```bash
  cd student-management-system
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Database Migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py load_defaults 
```

Start the server

```bash
  python manage.py runserver
```
## Run Locally

Clone the project

```bash
  git clone https://github.com/eaarda/student-management-system.git
```

Go to the project directory

```bash
  cd student-management-system
```

Start the server

```bash
  docker-compose up --build
```


### Admin User
An admin user is created by default after loading defaults command:

- Email: admin@admin.com
- Password: admin1234




### Documentation


```http
  GET /api/swagger
  GET /api/redoc
```


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.elifarda.dev/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/eaadev)

