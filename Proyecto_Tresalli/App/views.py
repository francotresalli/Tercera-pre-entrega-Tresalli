from django.shortcuts import render, redirect
from App.models import Torneo, Equipo, Jugador, EstadisticasJugador, Scout
from App.forms import TorneoFormulario, EquipoFormulario, JugadorFormulario, EstadisticasJugadorFormulario, ScoutFormulario, BuscarJugadorFormulario



def inicio(request):
    return render(request, 'App/inicio.html')

def torneos(request):
    torneos = Torneo.objects.all()  # Obtiene todos los torneos
    return render(request, 'App/torneos.html', {'torneos': torneos})

def equipos(request):
    equipos = Equipo.objects.all()  # Obtiene todos los equipos
    return render(request, 'App/equipos.html', {'equipos': equipos})


def jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'App/jugadores.html', {'jugadores': jugadores})

def estadisticas(request):
    stats = EstadisticasJugador.objects.all()  # Obtener todas las estadísticas
    return render(request, 'App/estadisticas.html', {'stats': stats})

def scouting(request):
    scouts = Scout.objects.all()  # Obtener todos los registros de scouts
    return render(request, 'App/scouting.html', {'scouts': scouts})


def crear_torneo(request):
    if request.method == 'POST':
        formulario = TorneoFormulario(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            descripcion = formulario.cleaned_data['descripcion']
            fecha_inicio = formulario.cleaned_data['fecha_inicio']
            fecha_fin = formulario.cleaned_data['fecha_fin']
            ubicacion = formulario.cleaned_data['ubicacion']
            Torneo.objects.create(nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, ubicacion=ubicacion)
            return redirect('torneos')
    else:
        formulario = TorneoFormulario()
    return render(request, 'App/crear_torneo.html', {'formulario': formulario})

def crear_equipo(request):
    if request.method == 'POST':
        formulario = EquipoFormulario(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            torneo = formulario.cleaned_data['torneo']
            entrenador = formulario.cleaned_data['entrenador']
            ciudad = formulario.cleaned_data['ciudad']
            Equipo.objects.create(nombre=nombre, torneo=torneo, entrenador=entrenador, ciudad=ciudad)
            return redirect('equipo') 
    else:
        formulario = EquipoFormulario()  # Esto debe estar en su propio bloque `else`

    return render(request, 'App/crear_equipo.html', {'formulario': formulario})


def crear_jugador(request):
    if request.method == 'POST':
        formulario = JugadorFormulario(request.POST)
        if formulario.is_valid():
            equipo = formulario.cleaned_data['equipo']
            nombre = formulario.cleaned_data['nombre']
            apellido = formulario.cleaned_data['apellido']
            posicion = formulario.cleaned_data['posicion']
            fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento']
            Jugador.objects.create(equipo=equipo, nombre=nombre, apellido=apellido, posicion=posicion, fecha_nacimiento=fecha_nacimiento)
            return redirect('jugadores')  # Cambia por la URL deseada
    else:
        formulario = JugadorFormulario()  # Esto debe estar en su propio bloque `else`

    return render(request, 'App/crear_jugador.html', {'formulario': formulario})


def crear_estadisticas(request):
    if request.method == 'POST':
        formulario = EstadisticasJugadorFormulario(request.POST)
        if formulario.is_valid():
            jugador = formulario.cleaned_data['jugador']
            partido = formulario.cleaned_data['partido']
            goles = formulario.cleaned_data['goles']
            asistencias = formulario.cleaned_data['asistencias']
            tarjetas_amarillas = formulario.cleaned_data['tarjetas_amarillas']
            tarjetas_rojas = formulario.cleaned_data['tarjetas_rojas']
            minutos_jugados = formulario.cleaned_data['minutos_jugados']
            fecha_partido = formulario.cleaned_data['fecha_partido']
            EstadisticasJugador.objects.create(
                jugador=jugador,
                partido=partido,
                goles=goles,
                asistencias=asistencias,
                tarjetas_amarillas=tarjetas_amarillas,
                tarjetas_rojas=tarjetas_rojas,
                minutos_jugados=minutos_jugados,
                fecha_partido=fecha_partido,
            )
            return redirect('estadisticas')  # Asegúrate de tener esta URL definida
    else:
        formulario = EstadisticasJugadorFormulario()

    return render(request, 'App/crear_estadisticas.html', {'formulario': formulario})

    

def crear_scout(request):
    if request.method == 'POST':
        formulario = ScoutFormulario(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            jugador_interesado = formulario.cleaned_data['jugador_interesado']
            Scout.objects.create(
                nombre=nombre,
                email=email,
                jugador_interesado=jugador_interesado,
            )
            return redirect('scouting')  # Asegúrate de que esta URL esté definida.
    else:
        formulario = ScoutFormulario()

    return render(request, 'App/crear_scout.html', {'formulario': formulario})


def buscar_jugador(request):
    if request.method == 'POST':
        formulario = BuscarJugadorFormulario(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            jugadores = Jugador.objects.filter(nombre__icontains=nombre)
            return render(request, 'App/busqueda_correcta.html', {'formulario': formulario, 'jugadores': jugadores})
    else:
        formulario = BuscarJugadorFormulario()
    
    return render(request, 'App/buscar_jugador.html', {'formulario': formulario})

