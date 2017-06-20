# Planteamiento del problema
El objetivo del reto es desarrollar un gestor sencillo de contactos. Debe ser un interfaz gráfico y debe tener la siguiente funcionalidad;
- La información de un contacto será; nombre, apellidos, teléfono, dirección (calle, población, código postal y país), dirección de correo y página web
- Los datos de los contactos tienen que almacenarse en una base de datos SQL
- Interfaz de consulta con la posibilidad de filtrar por nombre, dirección de correo, código postal, población y país
- Interfaz de alta / edición de registros
- Para rellenar la dirección en el interfaz de alta / edición se utilizará el API de Google Places https://developers.google.com/places/?hl=es-419

# Resolución
Para llevar a cabo los requisitos se ha desarrollado una aplicación web de gestión de contactos que permite almacenar, eliminar, consultar y actualizar contactos.

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
