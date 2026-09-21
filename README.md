# 📅 Agenda de Reuniones

Aplicación web desarrollada con **Django** para gestionar reuniones de manera organizada, permitiendo registrar, consultar, modificar y eliminar reuniones, además de clasificarlas por tipo y estado.

Este proyecto forma parte de mi proceso de aprendizaje en desarrollo web con Python y Django, y representa una aplicación práctica de conceptos como modelos, relaciones entre datos, formularios, vistas, autenticación, operaciones CRUD y consultas mediante el ORM de Django.

---

## 🚀 Funcionalidades

### 📌 Gestión de Reuniones
La aplicación permite realizar el ciclo CRUD completo de reuniones:
- **Crear** nuevas reuniones.
- **Consultar** el detalle de una reunión.
- **Editar** reuniones existentes.
- **Eliminar** reuniones.
- Registrar fecha, hora, lugar, participantes y observaciones.
- Clasificar reuniones según su estado:
  - 🟡 **Pendiente**
  - 🟢 **Realizada**
  - 🔴 **Cancelada**

### 🗂️ Tipos de Reunión
Permite administrar diferentes categorías/tipos de reuniones mediante operaciones CRUD:
- Crear, consultar, editar y eliminar tipos de reunión.
- Agregar una descripción detallada para cada tipo.

### 🔎 Búsqueda y Filtros
La agenda incorpora herramientas avanzadas para facilitar la consulta de información:
- Filtrar por tipo de reunión y estado.
- Buscar de forma dinámica por título o participantes mediante consultas `Q` de Django.

### 📊 Panel de Inicio
La página principal presenta un resumen ejecutivo asociado al usuario autenticado:
- Total de reuniones.
- Reuniones pendientes y canceladas.
- Total de tipos de reunión configurados.
- Próxima reunión registrada.

---

## 🗄️ Modelo de Datos

El proyecto utiliza el sistema de modelos y el ORM nativo de Django. La estructura relacional se define a continuación:

```text
Usuario (Django Auth)
       │
       │ 1:N
       ▼
    Reunión
       │
       │ N:1
       ▼
Tipo de Reunión
```text

---

## 🔐 Autenticación
Las principales vistas de la aplicación requieren que el usuario haya iniciado sesión.
Esto se implementa mediante el decorador:
@login_required

from django.contrib.auth.decorators import login_required

@login_required
def lista_reuniones(request):
    ...
De esta manera, las operaciones de la agenda quedan asociadas al usuario autenticado.

---

## 🛠️ Tecnologías utilizadas

Python
Django 5.2
Django ORM
HTML / CSS
Bootstrap
Base de datos relacional
Gunicorn
Git / GitHub
Render para despliegue

---

## 📁 Estructura Principal del Proyecto

agenda_reuniones/
│
├── agenda/               # Aplicación principal de la agenda
│   ├── migrations/       # Historial de migraciones de base de datos
│   ├── templates/        # Plantillas HTML (vistas del usuario)
│   ├── forms.py          # Formularios basados en ModelForm
│   ├── models.py         # Definición de modelos (Reunion, TipoReunion)
│   ├── urls.py           # Rutas internas de la aplicación
│   └── views.py          # Lógica de negocio y controladores
│
├── config/               # Configuración global del proyecto
│   ├── settings.py       # Ajustes principales de Django
│   ├── urls.py           # Enrutamiento general
│   └── wsgi.py           # Configuración del servidor de producción
│
├── build.sh              # Script de construcción para el despliegue
├── manage.py             # CLI de comandos de Django
├── Procfile              # Instrucciones para el servidor Gunicorn
└── requirements.txt      # Lista de dependencias del proyecto

El proyecto incluye un script build.sh que instala las dependencias, recopila los archivos estáticos (collectstatic) y ejecuta las migraciones (migrate) automáticamente durante el proceso de despliegue.

---

## ⚙️ Instalación local

1.- Clonar el repositorio:
git clone https://github.com/elbaneira/agenda_reuniones.git

Ingresar al proyecto:
cd agenda_reuniones

Crear y activar un entorno virtual:
python -m venv venv

En Windows:
venv\Scripts\activate

Instalar las dependencias:
pip install -r requirements.txt

Ejecutar las migraciones:
python manage.py migrate

Iniciar el servidor:
python manage.py runserver

Luego abrir en el navegador:
http://127.0.0.1:8000/

---

## 🌐 Despliegue
El proyecto fue preparado para ser desplegado en un entorno de hosting utilizando Gunicorn y un script de construcción para Django.
La configuración actual incluye:
build.sh
Procfile
requirements.txt

El despliegue puede realizarse utilizando Render conectado al repositorio de GitHub.
🔗 Repositorio: github.com/elbaneira/agenda_reuniones

---

## 📚 Aprendizajes del proyecto
Este proyecto me permitió reforzar conceptos de desarrollo web con Django, especialmente:
Creación y organización de un proyecto Django.
Creación de aplicaciones.
Modelado de datos.
Relaciones mediante claves foráneas.
Django ORM.
Formularios con ModelForm.
Operaciones CRUD.
Autenticación de usuarios.
Consultas y filtros.
Uso de Q para búsquedas.
Mensajes para informar el resultado de las operaciones.
Preparación de una aplicación para despliegue.

---

## 👩‍💻 Autora
Elba Neira
Desarrollo Full Stack · Python · Django · Bases de Datos
Un proyecto más en el camino de convertir el aprendizaje en proyectos reales.

---
© 2026 Elba Neira
