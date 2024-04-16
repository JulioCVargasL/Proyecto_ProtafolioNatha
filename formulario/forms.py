from django       import forms
from django.forms import ModelForm
from .models      import Status,Pagos,Event_type,Sesion,Usuario,Administrador, Login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms  import UserCreationForm
from django.urls                import reverse_lazy
from django.views.generic       import CreateView

class StatusForm(ModelForm):
  class Meta: 
    model     = Status
    fields    = ("__all__")

class PagosForm(ModelForm):
  class Meta:
    model   = Pagos
    fields  = ["cotizacion","pay_comment","pay_status","pay_date"]
    widgets = {
      "cotizacion":   forms.NumberInput(attrs={"class":"fomulario"}),
      "pay_comment":  forms.Textarea(attrs={"cols": 20, "rows": 5, "class":"fomulario"}),
      "pay_status":   forms.RadioSelect(attrs={"class": "formulario"}),
      "pay_date":     forms.DateInput(attrs={'type':'date',"class":"formulario"}),
    }

class Event_typeForm(ModelForm):
  class Meta:
    model   = Event_type
    fields  = ("__all__")

class SesionForm(ModelForm):
  class Meta:
    model   = Sesion
    fields  = ["ses_date","event_type","ses_comment","pagos"]
    widgets = {
      "ses_date":     forms.DateInput(attrs={'type':'date', "class": "formulario"}),
      "event_type":   forms.RadioSelect(attrs={"class":"formulario"}),  
      "ses_comment":  forms.Textarea(attrs={"cols": 20, "rows": 5, "class":"fomulario"}),
      "pagos":        forms.CheckboxSelectMultiple(attrs={"class": "formulario"})
    }

class UsuarioForm(ModelForm):
  class Meta:
    model   = Usuario
    fields  = ["user_name","user_email","user_doc","user_password","sesion"]
    widgets = {
      "user_name":      forms.TextInput(attrs={"class":"formulario", "max_length":50, "required":True}),
      "user_email":     forms.EmailInput(attrs={"class":"formulario"}),
      "user_doc":       forms.NumberInput(attrs={"class": "formulario"}),  
      "user_password":  forms.TextInput(attrs={"class":"formulario",'type':'password'}),
      
    }

class AdministradorForm(ModelForm):
  class Meta:
    model   = Administrador
    fields  = ("__all__")

class LoginForm(ModelForm):
  class Meta:
    model   = Login
    fields  = ("__all__")