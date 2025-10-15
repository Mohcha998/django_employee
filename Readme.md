# Employee Management System - Backend

Backend menggunakan **Django + MySQL + DRF** dengan **JWT Authentication** untuk sistem CRUD Master Karyawan.

---

## 🔹 Fitur

- Login / Logout JWT
- CRUD Master Karyawan
- MySQL Database
- Clean Architecture:
  - `domain` → Entity murni
  - `data` → Repositories & Serializers
  - `usecases` → Logic aplikasi
  - `presentation` → Views / API Views
- Unit test untuk models, usecases, views

---

## 🔹 Struktur Project

.
├── employee_backend
│ ├── **init**.py
│ ├── **pycache**
│ │ ├── **init**.cpython-313.pyc
│ │ ├── settings.cpython-313.pyc
│ │ ├── urls.cpython-313.pyc
│ │ └── wsgi.cpython-313.pyc
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── employees
│ ├── **init**.py
│ ├── **pycache**
│ │ ├── **init**.cpython-313.pyc
│ │ ├── admin.cpython-313.pyc
│ │ └── apps.cpython-313.pyc
│ ├── admin.py
│ ├── apps.py
│ ├── data
│ │ ├── **pycache**
│ │ │ ├── repositories.cpython-313.pyc
│ │ │ └── serializers.cpython-313.pyc
│ │ ├── repositories.py
│ │ └── serializers.py
│ ├── domain
│ │ ├── **pycache**
│ │ │ └── models.cpython-313.pyc
│ │ └── models.py
│ ├── migrations
│ │ ├── **init**.py
│ │ ├── **pycache**
│ │ │ ├── **init**.cpython-313.pyc
│ │ │ └── 0001_initial.cpython-313.pyc
│ │ └── 0001_initial.py
│ ├── presentation
│ │ ├── **pycache**
│ │ │ ├── models_django.cpython-313.pyc
│ │ │ └── views.cpython-313.pyc
│ │ ├── models_django.py
│ │ └── views.py
│ ├── tests
│ └── usecases
│ ├── **pycache**
│ │ └── employee_usecases.cpython-313.pyc
│ └── employee_usecases.py
├── manage.py
└── Readme.md

---

## 🔹 Setup Backend (Mac)

### Prasyarat

- Python 3.13
- MySQL 8+
- pip / virtualenv
- Git

### Instalasi

```bash
# Clone project
git clone <repo-url>
cd employee_backend

# Buat virtualenv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Setting untuk database di setting.py

### Sesuaikan dengan database yang di gunakan dan namanya

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'employee_db',
'USER': 'employee_user',
'PASSWORD': 'password123',
'HOST': 'localhost',
'PORT': '3306',
}
}

### Migrasi dan Super User

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Menjalankan server

python manage.py runserver

### API ENDPOINT

Endpoint Method Keterangan
/api/token/ POST Login, dapat access & refresh JWT
/api/token/refresh/ POST Refresh token
/api/employees/ GET List employees (auth required)
/api/employees/ POST Create employee
/api/employees/<id>/ GET Detail employee
/api/employees/<id>/ PUT Update employee
/api/employees/<id>/ DELETE Delete employee
