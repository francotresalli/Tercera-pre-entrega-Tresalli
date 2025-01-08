from django import forms

class TorneoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()
    ubicacion = forms.CharField(max_length=100)


class EquipoFormulario(forms.Form):  
    nombre = forms.CharField(max_length=100)
    torneo = forms.CharField(max_length=100)
    entrenador = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=100)
    jugadores = forms.CharField(max_length=100)


class JugadorFormulario(forms.Form):    
    equipo = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    posicion = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()


class EstadisticasJugadorFormulario(forms.Form):
    jugador = forms.CharField(max_length=100)
    partido = forms.CharField(max_length=100)
    goles = forms.IntegerField()
    asistencias = forms.IntegerField()
    tarjetas_amarillas = forms.IntegerField()
    tarjetas_rojas = forms.IntegerField()
    minutos_jugados = forms.IntegerField()
    fecha_partido = forms.DateField()


class ScoutFormulario(forms.Form):    
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    jugador_interesado = forms.CharField(max_length=100)


class BuscarJugadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    
    
