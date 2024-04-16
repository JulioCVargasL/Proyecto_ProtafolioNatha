from django.contrib import admin
from .models import Usuario
# Register your models here.

class AdministrarUsuarios(admin.ModelAdmin):
  list_display = ('user_name','user_email','user_doc','user_password','sesion')
  search_fields = ('user_name','user_email','user_doc')
  list_filter   = ('user_doc','user_name')

admin.site.register(Usuario, AdministrarUsuarios)