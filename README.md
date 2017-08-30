La aplicación utiliza las siguientes tecnologías:
  - Lenguaje Python con Framework Django
  - Bases de datos SQlite3 en Local y PostgreSQL en producción
  - Heroku como plataforma de hosting
  - API Javascript de Google Places

# Link a la aplicación en heroku
    
### https://contacts-agenda.herokuapp.com/


# Comando para correr la aplicación en local

Para probar la aplicación en local es necesario tener instalado python 3 y Django

Primero hacer las migraciones:

    $ python manage.py makemigrations
    $ python manage.py migrate

Por último poner en marcha el servidor:

    $ python manage.py runserver
