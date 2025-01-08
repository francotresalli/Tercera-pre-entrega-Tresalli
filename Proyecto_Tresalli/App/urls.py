from django.urls import path
from App import views


urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('torneos/', views.torneos, name='torneos'),
    path('equipos/', views.equipos, name='equipos'),
    path('jugadores/', views.jugadores, name='jugadores'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('scouting/', views.scouting, name='scouting'),
    path('crear_torneo/', views.crear_torneo, name='crear_torneo'),
    path('crear_equipo/', views.crear_equipo, name='crear_equipo'),
    path('crear_jugador/', views.crear_jugador, name='crear_jugador'),
    path('crear_estadisticas/', views.crear_estadisticas, name='crear_estadisticas'),
    path('crear_scout/', views.crear_scout, name='crear_scout'),
    path('buscar_jugador/', views.buscar_jugador, name='buscar_jugador'),
]