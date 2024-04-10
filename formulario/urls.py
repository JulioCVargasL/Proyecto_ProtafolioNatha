from django.urls    import path
from .              import views

urlpatterns = [
    path('registrar/', views.registrar, name="registrar"),
    path('registrar_pago/', views.registrar_pago, name="registrar_pago"),
    path('listar_pagos/', views.listar, name="listar_pagos"),
]