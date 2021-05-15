from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class ControladorUsuario(BaseUserManager):
    def create_user(self, username, nombres, apellido_paterno, tipo_contratacion, numero_empleado, tipo_usuario, email, numero_telefonico, foto,apellido_materno="", password=None):
        if not username:
            raise ValueError('Los usuarios necesitan un nombre de usuario válido.')
        usuario = self.model(
            username = username,
            nombres = nombres,
            apellido_paterno = apellido_paterno,
            apellido_materno = apellido_materno,
            tipo_contratacion = tipo_contratacion,
            numero_empleado = numero_empleado,
            tipo_usuario = tipo_usuario,
            email = email,
            numero_telefonico = numero_telefonico,
            foto = foto
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, username, nombres, apellido_paterno, apellido_materno, tipo_contratacion, numero_empleado, tipo_usuario, email, numero_telefonico, foto, password):
        usuario = self.create_user(
                username = username,
                nombres = nombres,
                apellido_paterno = apellido_paterno,
                apellido_materno = apellido_materno,
                tipo_contratacion = tipo_contratacion,
                numero_empleado = numero_empleado,
                tipo_usuario = tipo_usuario,
                email = email,
                numero_telefonico = numero_telefonico,
                foto = foto,
                password = password
                )
        usuario.admin = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    CATEGORIAS_USUARIOS = (
        ('Administrador', 'Administrador'),
        ('Monitor', 'Monitor'),
        ('Supervisor de módulo', 'Supervisor de módulo'),
        ('Personal de módulo', 'Personal de módulo'),
    )
    
    username = models.CharField("Nombre de usuario", max_length=100, unique=True)
    nombres = models.CharField("Nombre(s)", max_length=200)
    apellido_paterno = models.CharField("Apellido paterno", max_length=200)
    apellido_materno = models.CharField("Apellido materno", max_length=200, blank=True, null=True)
    tipo_contratacion = models.CharField("Tipo de contratación", max_length=50)
    numero_empleado = models.PositiveIntegerField("Número de empleado")
    tipo_usuario = models.CharField("Tipo de usuario", max_length=21, choices=CATEGORIAS_USUARIOS)
    email = models.EmailField("Correo electrónico", max_length=100, unique=True)
    numero_telefonico = models.CharField("Número telefónico", max_length=15)
    foto = models.ImageField("Sube una fotografía", blank=True, default="guest.png")
    
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default= False)
    staff = models.BooleanField(default=True)

    objects = ControladorUsuario()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombres', 'apellido_paterno', 'apellido_materno', 'tipo_contratacion', 'numero_empleado', 'tipo_usuario', 'email', 'numero_telefonico', 'foto']

    def __str__(self):
        return f'{self.nombres}, {self.apellido_paterno}'
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def delete(self):
        self.active = False
        self.save()
    
    def reactive(self):
        self.active = True
        self.save()

    @property
    def is_staff(self):
        return self.staff