from django.urls    import path, include

from .              import views

urlpatterns = [
    path("admin_dashboard/",views.admin_dashboard,name="admin_dashboard"),
    path("signup/",         views.signup,         name="signup"),
    path('event_type/',     views.event_type,     name="event_type"),
    path('crear_status/',   views.crear_status,   name="crear_status"),
    path('agendar/',        views.agendar,        name="agendar"),
    path('login/',          views.login,          name="login"),       
]