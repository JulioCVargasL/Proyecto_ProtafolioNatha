from django.urls    import path
from .              import views

urlpatterns = [
    path('registrar_pago/',    views.registrar_pago,   name="registrar_pago"),
    path('listar_pagos/',      views.listar,           name="listar_pagos"),
    path('show_editar_pago/',  views.show_editar_pago, name="show_editar_pago"),
    path('editar_pago/',       views.editar_pago,      name="editar_pago"),
    path('delete_pago/<int:id>',views.delete_pago, name="eliminar_pago"), 
]