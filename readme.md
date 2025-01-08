Proyecto: Plataforma de Análisis y Scouting para Fútbol Amateur

Descripción

Este proyecto es una aplicación web desarrollada en Django 4.2 que permite la gestión de equipos, jugadores, estadísticas, y scouting en torneos de fútbol amateur. Incluye funcionalidades para:

Crear, buscar y gestionar jugadores.

Administrar equipos y sus integrantes.

Registrar estadísticas de partidos.

Facilitar el scouting de jugadores.

Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local:

Clonar el repositorio:

git clone <URL-del-repositorio>
cd <nombre-del-directorio>

Crear un entorno virtual e instalar dependencias:
Asegúrate de tener pipenv instalado.

pipenv install
pipenv shell

Configurar la base de datos:
Por defecto, se utiliza SQLite. Si deseas cambiar a otra base de datos, actualiza la configuración en settings.py.

Realizar las migraciones:

python manage.py makemigrations
python manage.py migrate

Cargar datos iniciales (opcional):
Si se incluye un archivo de datos iniciales:

python manage.py loaddata datos_iniciales.json

Ejecutar el servidor de desarrollo:

python manage.py runserver

Accede a la aplicación en http://127.0.0.1:8000/.

Dependencias principales

Python 3.11

Django 4.2

pipenv

Estructura del proyecto

App: Contiene las aplicaciones principales del proyecto.

Templates: Archivos HTML para las vistas de la aplicación.

Static: Archivos estáticos como CSS, JavaScript e imágenes.

Funcionalidades principales

Gestor de Jugadores:

Crear, buscar y visualizar información de jugadores.

Administración de Equipos:

Crear equipos y asignar jugadores a estos.

Estadísticas:

Registrar y visualizar estadísticas de los partidos.

Scouting:

Facilitar el proceso de scouting mediante un formulario.

Uso

Crear Jugador

Ve a la sección de "Crear Jugador".

Completa el formulario con la información requerida.

Haz clic en "Enviar".

Buscar Jugador

Ve a la sección de "Buscar Jugador".

Ingresa el criterio de búsqueda en el formulario.

Revisa los resultados.

Crear Equipo

Ve a la sección de "Crear Equipo".

Completa el formulario con el nombre, torneo, entrenador y ciudad.

Haz clic en "Enviar".