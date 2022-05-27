
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

# Create your models here.

#clase para crear una cuenta de administrador
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager): #<-- cuenta de administrador
    def create_user(self, nombre, apellido, username, email, password=None):
        
        if not email:
            raise ValueError('El usuario debe tener un email')

        if not username:
            raise ValueError('El usuario debe tener un username')

        #se guardara todo en el objeto user
        user = self.model( 
            email = self.normalize_email(email),
            username = username,
            nombre = nombre,
            apellido = apellido,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  nombre, apellido, username, email, password):
       
       
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            nombre = nombre,
            apellido = apellido,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user

class Cuenta(AbstractBaseUser):
    # al crear  los ususarios  uso obligatorio
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    numero_telefonico = models.CharField(max_length=50)

    #Campos atributos de django

    fecha_registro = models.DateTimeField(auto_now_add=True) ##<- varaible que ve la fecha que se crea el usuario
    ultima_conexion= models.DateTimeField(auto_now_add=True)##<-- varaible en la cual registra la ultima vez que  entro el usuario
    is_admin=models.BooleanField(default=False)##<-- verifica  si es administrador
    is_staff= models.BooleanField(default=False)#<--es parte del equipo
    is_superadmin=models.BooleanField(default=False)#se verifica si es super admin

    USERNAME_FIELD='email' # cada vez  se ingrese  al login tomara el email
    REQUIRED_FIELDS =['username', 'nombre', 'apellido']#se requiere  campos  obligatorios
    
    #se hace una instancia de  la clase
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
