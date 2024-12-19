from django.db import models

# Modelo para representar un automóvil
class Project(models.Model):
    name = models.CharField(max_length=200)        # Nombre del vehículo (por ejemplo, "Ford Mustang")
    brand = models.CharField(max_length=200)       # Marca del vehículo (por ejemplo, "Ford")
    model = models.CharField(max_length=200)       # Modelo del vehículo (por ejemplo, "2022")
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del vehículo, con dos decimales

    def __str__(self):
        return self.name  # Muestra el nombre del vehículo cuando se consulte un proyecto
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
        
    def __str__(self):
        return self.title