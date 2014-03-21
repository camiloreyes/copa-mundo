from django.db import models

# Create your models here.

POSICIONES = (
    ('seleccione', 'Seleccione'),
    ('arquero', 'Arquero'),
    ('defensa', 'Defensa'),
    ('volante', 'Volante'),
    ('delantero', 'Delantero'),
)

class Continente(models.Model):
    nombreContinente = models.CharField(max_length=50)
    

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    continente = models.ForeignKey(Continente)
    tecnico = models.CharField(max_length=60)

class Jugador(models.Model):
    nombreJugador = models.CharField(max_length=60)
    posicion = models.CharField(choices=POSICIONES, default= 'seleccione', max_length=10)
    #foto  = models.ImageField(upload_to='imagen', verbose='foto', null=True,)
    def __unicode__(self):
        return self.nombreJugador

