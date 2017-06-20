from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
from django.contrib.auth.models import User


class Contacto(models.Model):
    nombre = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    telefono = models.IntegerField()
    email= models.EmailField()
    pagina_web = models.CharField(max_length=250)

    calle = models.CharField(max_length=250)
    provincia = models.CharField(max_length=250)
    pais = models.CharField(max_length=250)
    codigo_postal = models.CharField(max_length=250)


    def get_absolute_url(self):
        return reverse('contacts:detail',kwargs={'pk': self.pk})

    def __str__(self):
        return self.nombre + " " + self.apellidos
