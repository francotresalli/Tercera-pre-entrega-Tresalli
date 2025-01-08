from django.db import models


class Torneo(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    torneo = models.ForeignKey(Torneo, related_name='equipos', on_delete=models.CASCADE)
    entrenador = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    jugadores = models.ManyToManyField('Jugador', related_name='equipos')

    def __str__(self):
        return self.nombre
    
class Jugador(models.Model):
     equipo = models.ForeignKey(Equipo, related_name='jugadores_del_equipo', on_delete=models.CASCADE)
     nombre = models.CharField(max_length=255)
     apellido = models.CharField(max_length=255)
     posicion = models.CharField(max_length=50)
     fecha_nacimiento = models.DateField()

     def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class EstadisticasJugador(models.Model):
     jugador = models.ForeignKey(Jugador, related_name='estadisticas', on_delete=models.CASCADE)
     partido = models.CharField(max_length=255)
     goles = models.IntegerField(default=0)
     asistencias = models.IntegerField(default=0)
     tarjetas_amarillas = models.IntegerField(default=0)
     tarjetas_rojas = models.IntegerField(default=0)
     minutos_jugados = models.IntegerField(default=0)
     fecha_partido = models.DateField()

     def __str__(self):
        return f"Estadísticas de {self.jugador} en {self.partido}"


class Scout(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    jugador_interesado = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
