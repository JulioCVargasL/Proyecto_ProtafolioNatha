from django       import forms
from django.forms import ModelForm
from .models      import Status,Pagos,Event_type,Sesion,Usuario,Administrador

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
    fields  = ("__all__")

class AdministradorForm(ModelForm):
  class Meta:
    model   = Administrador
    fields  = ("__all__")

