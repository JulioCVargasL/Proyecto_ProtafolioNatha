from django       import forms
from django.forms import ModelForm
from .models      import Pagos,Event_type,Sesion,Usuario,Administrador

class PagosForm(ModelForm):
  class Meta:
    model   = Pagos
    fields  = ["cotizacion","pay_comment","pay_status","pay_date"]
    widgets = {
      "cotizacion":   forms.NumberInput(attrs={"class":"fomulario"}),
      "pay_comment":  forms.Textarea(attrs={"cols": 80, "rows": 20, "class":"fomulario"}),
      "pay_status":   forms.MultipleChoiceField
    }

class Event_typeForm(ModelForm):
  class Meta:
    model   = Event_type
    fields  = ("__all__")

class SesionForm(ModelForm):
  class Meta:
    model   = Sesion
    fields  = ("__all__")

class UsuarioForm(ModelForm):
  class Meta:
    model   = Usuario
    fields  = ("__all__")

class AdministradorForm(ModelForm):
  class Meta:
    model   = Administrador
    fields  = ("__all__")

