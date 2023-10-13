from django.db import models
from django.core.validators import MinLengthValidator

class Usuario(models.Model):
    nombre = models.CharField(max_length=15, validators=[
            MinLengthValidator(limit_value=5, 
                               message="El nombre de usuario debe tener al menos 5 caracteres.")
        ])
    
    email = models.EmailField()
    contraseña = models.CharField(max_length=10, validators=[
            MinLengthValidator(limit_value=5, 
                               message="Su contraseña debe tener al menos 5 caracteres.")
        ])
    
    def __str__(self) -> str:
        return self.nombre