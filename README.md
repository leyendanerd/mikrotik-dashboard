# Mikrotik Dashboard

Este proyecto provee una pequeña aplicación en Django para administrar dispositivos MikroTik.
La interfaz usa Bootstrap para ofrecer un diseño agradable.

## Requisitos
- Python 3.12
- Django 5

## Instalación sin Docker
1. Instalar dependencias:
   ```bash
   pip install Django==5.0.1
   ```
2. Crear las migraciones y la base de datos:
   ```bash
   python manage.py migrate
   ```
3. Ejecutar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

Accede a `http://localhost:8000/` para ver la lista de dispositivos y a `http://localhost:8000/admin/` para el panel de administración.
Si deseas iniciar sesión y ver la lista de usuarios navega a `http://localhost:8000/accounts/login/`.

## Uso con Docker

Para ejecutar la aplicación junto a una base de datos Postgres se provee un `docker-compose.yml`.

1. Construye las imágenes y levanta los servicios:
   ```bash
   docker-compose up --build
   ```
2. Accede a `http://localhost:8000/` para usar la aplicación.

