from django.urls    import path
from .              import views

urlpatterns = [
    path('registrar/', views.regitrar, name="registrar"),
]