from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('candidato', 'Candidato'),
        ('reclutador', 'Reclutador'),
        ('administrador', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES, default='candidato')

    def __str__(self):
        return f"{self.username} ({self.rol})"
class EmpresaCliente(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Vacante(models.Model):
    ESTADOS = [
        ('abierta', 'Abierta'),
        ('cerrada', 'Cerrada'),
        ('en_proceso', 'En Proceso'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  
    empresa = models.CharField(max_length=150)
    puesto = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    requisitos = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='abierta')
    def __str__(self):
        return self.puesto


class Candidato(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    experiencia = models.TextField(blank=True)
    habilidades = models.TextField(blank=True)
    disponibilidad = models.BooleanField(default=True)
    cv = models.FileField(upload_to="cv/")

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class InformeRiesgo(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nivel_riesgo = models.CharField(max_length=50)
    observaciones = models.TextField()
    fecha_emision = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Informe de {self.candidato} ({self.nivel_riesgo})"