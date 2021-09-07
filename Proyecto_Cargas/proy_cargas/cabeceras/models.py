from django.db import models

class Archivo(models.Model):
    Titulo = models.CharField(max_length = 200)
    ArchivoSubido = models.FileField(upload_to = "Archivos Cargados/")
    FechaDeSubida = models.DateTimeField(auto_now = True)

    def publish(self):
        self.save()
        
    def __str__(self):
        return self.Titulo