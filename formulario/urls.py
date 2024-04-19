from django.urls    import path, include

from .              import views

urlpatterns = [
    path("admin_dashboard/",views.admin_dashboard,name="admin_dashboard"),
    path('admin_users/',    views.admin_users,    name='admin_users'),
    path("signup/",         views.signup,         name="signup"),
    path('event_type/',     views.event_type,     name="event_type"),
    path('crear_status/',   views.crear_status,   name="crear_status"),
    path('agendar/',        views.agendar,        name="agendar"),
    path('lista_sesiones/', views.sesiones_list,  name="lista_sesiones"),
    path('delete_sesion/<int:id>', views.delete_sesion,   name="delete_sesion"),
    path('editar_sesion/<int:id>', views.edit_sesion,     name="editar_sesion"), 
    path('login/',          views.login,          name="login"),
    path("lista_usuarios/", views.user_list,      name="lista_usuarios"),
    path('delete_user/<int:id>', views.delete_user,   name="delete_user"),
    path('editar_user/<int:id>', views.edit_user,     name="editar_user"),   

]