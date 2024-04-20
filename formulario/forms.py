from django       import forms
from django.forms import ModelForm
from .models      import Status,Event_type,Sesion,Usuario,Login
# from django.contrib.auth.decorators import login_required

class LoginForm(ModelForm):
  class Meta:
    model   = Login
    fields  = ("__all__")

class UsuarioForm(ModelForm):

  class Meta:
    model   = Usuario
    fields  = ["user_name","user_email","user_doc","user_phone"]
    widgets = {
      "user_name":      forms.TextInput(  attrs={"class": "user_name formulario", "name":"user_name", "id":"user_name", "max_length":50, "required":True, "placeholder":"Eje. Pedro Picapiedra"}),
      "user_email":     forms.EmailInput( attrs={"class": "user_email formulario", "name":"user_email","id":"user_email","placeholder":"Eje. E@ejemplo.com"}),
      "user_phone":     forms.NumberInput(attrs={"class": "user_phone formulario", "name":"user_phone","id":"user_phone","placeholder":"Eje. 123-456-7890"}),
      "user_doc":       forms.NumberInput(attrs={"class": "user_doc formulario", "name":"user_doc",  "id":"user_doc","placeholder":"Eje. 1065788789"}),  
    }

class StatusForm(ModelForm):
  class Meta: 
    model   = Status
    fields  = ["nombre"]

class Event_typeForm(ModelForm):
  class Meta:
    model   = Event_type
    fields  = ["type"]

class SesionForm(ModelForm):
  class Meta:
    model   = Sesion
    fields  = ["ses_date","event_type","ses_comment","usuario","cotizacion","pay_date","pay_status"]
    widgets = {
      "usuario":      forms.Select(     attrs={"class": "formulario", "name":"usuario",     "id":"usuario"}),
      "event_type":   forms.Select(     attrs={"class": "formulario", "name":"event_type",  "id":"event_type"}),  
      "ses_date":     forms.DateInput(  attrs={"class": "formulario", "name":"ses_date",    "id":"ses_date",'type':'date'}),
      "cotizacion":   forms.NumberInput(attrs={"class": "formulario", "name":"cotizacion",  "id":"cotizacion", "placeholder":"Eje. 100.000"}),
      "pay_status":   forms.RadioSelect(attrs={"class": "formulario", "name":"pay_status",  "id":"pay_status", }),
      "pay_date":     forms.DateInput(  attrs={"class": "formulario", "name":"pay_date",    "id":"pay_date",'type':'date'}),
      "ses_comment":  forms.Textarea(   attrs={"class": "formulario", "name":"ses_comment", "id":"ses_comment","cols": 20, "rows": 5 , "placeholder":"Eje. Lorem ipsum dolor sit amet consectetur adipisicing elit. "}),
    }

