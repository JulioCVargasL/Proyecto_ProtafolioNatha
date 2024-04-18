from django.db  import models
from datetime   import date
from django.contrib.auth.decorators import login_required
#la linea 2 se tre para dar funcionalidad a Fecha de registro de la tabla Usuarios

# Create your models here.

class Login(models.Model):
  name            = models.CharField(max_length=50)
  password        = models.CharField(max_length=50)

# cuando creamos una clase su nombre debe empezar en mayuscula
class Usuario(models.Model):

  # user_ID         = models.AutoField(primary_key= True)
  user_doc        = models.IntegerField(verbose_name='Numero de documento')
  user_name       = models.CharField(max_length=40, blank= False, null= False,verbose_name= 'Nombre')
  user_email      = models.EmailField(verbose_name='Correo electronico')
  user_phone      = models.IntegerField(verbose_name='Numero de teléfono')
  fecha_registro  = models.DateTimeField (verbose_name='Fecha de registro',auto_now_add=True)
  def __str__(self):
    return self.user_name     

# @login_required
class Status(models.Model):
  nombre    = models.CharField(max_length=30, null=False, blank=False,verbose_name='Nuevo estado de pago')
  def __str__(self):
    return self.nombre

class Event_type(models.Model):
  type      = models.CharField(max_length=30, null=False, blank=False,verbose_name='Nuevo evento')
  def __str__(self):
    return self.type
  
class Sesion(models.Model):

  # ses_ID          = models.AutoField(primary_key= True)
  ses_date        = models.DateTimeField(verbose_name='Fecha del evento')
  ses_comment     = models.TextField(verbose_name='Comentarios')
  cotizacion      = models.IntegerField(verbose_name='Cotizacion')
  pay_date        = models.DateTimeField(verbose_name='Fecha de pago')
  # Foreing Key(s) Relacion uno a muchos
  usuario         = models.ForeignKey(Usuario, on_delete=models.PROTECT,verbose_name='Cliente')  
  event_type      = models.ForeignKey(Event_type, on_delete=models.PROTECT,verbose_name='Tipo de evento')
  pay_status      = models.ForeignKey(Status, on_delete=models.PROTECT,verbose_name='Estado de pago')
 



