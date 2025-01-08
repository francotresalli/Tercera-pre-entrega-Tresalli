from django.contrib import admin
from App.models import *

# Register your models here.
@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'ubicacion')
    search_fields = ('nombre', 'ubicacion')
    

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'torneo', 'entrenador', 'ciudad')
    search_fields = ('nombre', 'ciudad')
    list_filter = ('torneo', 'ciudad')

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'equipo', 'posicion', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellido', 'equipo__nombre')
    list_filter = ('equipo', 'posicion')

    @admin.register(EstadisticasJugador)
    class EstadisticasJugadorAdmin(admin.ModelAdmin):
        list_display = ('jugador', 'partido', 'goles', 'asistencias', 'tarjetas_amarillas', 'tarjetas_rojas', 'minutos_jugados', 'fecha_partido')
        search_fields = ('jugador__nombre', 'jugador__apellido', 'partido')
        list_filter = ('partido', 'fecha_partido')

@admin.register(Scout)
class ScoutAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'jugador_interesado')
    search_fields = ('nombre', 'jugador_interesado')

