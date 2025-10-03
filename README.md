# HRM Final Project

Proyecto Django completo de Recursos Humanos con:
- Login y roles (candidato, reclutador, administrador)
- CRUD de Vacantes, Candidatos e Informes de Riesgo
- Gestión de usuarios y roles
- Subida de CV
- Plantilla base con paleta de colores

## Pasos para correrlo
1. Crear entorno virtual e instalar Django:
   ```bash
   pip install django
   ```
2. Migrar la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Crear superusuario:
   ```bash
   python manage.py createsuperuser
   ```
4. Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```
