from django.db  import models
from datetime   import date

#la linea 2 se tre para dar funcionalidad a Fecha de registro de la tabla Usuarios

# Create your models here.

# cuando creamos una clase su nombre debe empezar en mayuscula

class Pagos(models.Model):

  STATUS_OPTIONS = [
    ("Pendiente",     "Opcion 1"),
    ("Primer pago",   "Opcion 2"),
    ("Pago completo", "Opcion 3"),
  ]

  # pay_ID        = models.AutoField(primary_key= True)
  cotizacion    = models.IntegerField()
  pay_comment   = models.TextField()
  pay_status    = models.CharField(choices=STATUS_OPTIONS, max_length=20) 
  pay_date      = models.DateTimeField()

class Sesion(models.Model):

  EVENT_TYPE    = [
    ("Boda",                "Opcion 1"),
    ("Bautizo",             "Opcion 2"),
    ("Revelacion de sexo",  "Opcion 3"),
    ("Cumpleaños",          "Opcion 4"),
    ("Quince años",         "Opcion 5"),
    ("Evento empresarial",  "Opcion 6"),
  ]

  # ses_ID          = models.AutoField(primary_key= True)
  ses_date        = models.DateTimeField()
  ses_type        = models.CharField(choices=EVENT_TYPE, max_length=20)
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
