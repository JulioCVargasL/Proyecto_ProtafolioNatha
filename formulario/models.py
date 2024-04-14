from django.db  import models
from datetime   import date

#la linea 2 se tre para dar funcionalidad a Fecha de registro de la tabla Usuarios

# Create your models here.

# cuando creamos una clase su nombre debe empezar en mayuscula

class Status(models.Model):
  nombre      = models.CharField(max_length=20, null=False, blank=False)

class Pagos(models.Model):

  # STATUS_OPTIONS = [
  #   ("Pendiente",     "Opcion 1"),
  #   ("Primer pago",   "Opcion 2"),
  #   ("Pago completo", "Opcion 3"),
  # ]

  # pay_ID        = models.AutoField(primary_key= True)
  cotizacion    = models.IntegerField()
  pay_comment   = models.TextField()
  pay_status    = models.OneToOneField(Status, on_delete=models.PROTECT)
  pay_date      = models.DateTimeField()

class Event_type(models.Model):
  type      = models.CharField(max_length=50)
  def __str__(self):
    return self.type

class Sesion(models.Model):

  # ses_ID          = models.AutoField(primary_key= True)
  ses_date        = models.DateTimeField()
  event_type      = models.ForeignKey(Event_type, on_delete=models.PROTECT)
  ses_comment     = models.TextField()
  # Foreing Key(s) Relacion uno a uno
  pagos           = models.OneToOneField(Pagos, on_delete=models.PROTECT)  

class Usuario(models.Model):

  # user_ID         = models.AutoField(primary_key= True)
  fecha_registro  = models.DateField(default=date.today)
  user_doc        = models.IntegerField()
  user_name       = models.CharField(max_length=40, blank= False, null= False)
  user_email      = models.EmailField()
  user_password   = models.CharField(max_length=10, blank= False, null= False)
  # Foreing Key(s) Relacion uno a muchos
  sesion          = models.ForeignKey(Pagos, on_delete=models.PROTECT)          

class Administrador(models.Model):

  # admin_ID        = models.AutoField(primary_key= True)
  admin_doc       = models.IntegerField()
  admin_name      = models.CharField(max_length=40, blank= False, null= False)
  admin_email     = models.EmailField()
  admin_password  = models.CharField(max_length=10, blank= False, null= False)
  # Foreing Key(s) Relacion muchos a muchos
  usuario       = models.ManyToManyField(Usuario)
  # Esto crea una tabla pivote derivada de este tipo de relaciones 
