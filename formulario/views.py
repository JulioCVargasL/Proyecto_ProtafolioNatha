from django.shortcuts           import render, redirect, get_object_or_404
from django.http                import HttpResponse
from .forms                     import StatusForm,SesionForm,UsuarioForm,LoginForm,Event_typeForm
from .models                    import Usuario, Status, Event_type, Sesion, Login
from django.contrib.auth.decorators import login_required

# Create your views here.
# Vista pricipal admin
@login_required
def admin_dashboard(request):
  return render(request, '1.administrador/admin_dashboard.html')

# Administracion de usuarios
@login_required
def admin_users(request):
  return render(request, '1.administrador/admin_users.html')

@login_required
def admin_sesiones(request):
  return render(request, '1.administrador/admin_sesiones.html')

# Administrar Sesiones

def login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      form.save()
      form = LoginForm()
    return render(request, 'login.html', {
      'form':form,
    })
  else:
    form = LoginForm()
  return render(request, 'login.html', {
    'form':form,
  })

# Registrar Clientes

def signup(request):
  if request.method == 'POST':
    form = UsuarioForm(request.POST)
    if form.is_valid():
      form.save()
      form = UsuarioForm()
 
    return render(request, "registration/signup.html", {
      'form':form,
    })
  else:
    form = UsuarioForm()

  return render(request, 'registration/signup.html', {
    'form':form,
  })

# lista de usuarios

def user_list(request):
  lista_usuarios = Usuario.objects.all()
  return render(request, '1.administrador/lista_usuarios.html', {
    'lista_usuarios': lista_usuarios
  })

# eliminar usuario

def delete_user(request, id):
  eliminar = Usuario.objects.get(id=id)
  eliminar.delete()
  return redirect('lista_usuarios')

# Editar usuario

def edit_user(request, id):

  editar = get_object_or_404(Usuario, id = id)

  if request.method == 'POST':
    form = UsuarioForm(request.POST, instance=editar)
    if form.is_valid():
      form.save()

      # form = UsuarioForm(instance=editar)

    return redirect('lista_usuarios')
  
  else:

    form = UsuarioForm(instance=editar)

  return render(request, '1.administrador/editar_user.html',{
      'form':form,
      'editar':editar
    }
    )
# Crear y listar estados de pago

def crear_status(request):
  if request.method == 'POST':
    form1 = StatusForm(request.POST, prefix='form1')
    if form1.is_valid():
      form1.save()
      
      form1 = StatusForm()

    lista_status = Status.objects.all()    
    return render(request, '1.administrador/crear_status.html', {
      'form1':form1,
      'lista_status':lista_status
    })
    
  else:
    form1 = StatusForm(prefix='form1')

  lista_status = Status.objects.all() 

  return render(request, '1.administrador/crear_status.html', {
    'form':form1,
    'lista_status':lista_status
  })

# Crear y listar tipos de eventos

def event_type(request):
  if request.method == 'POST':
    form = Event_typeForm(request.POST)
    if form.is_valid():
      form.save()
      form = Event_typeForm()

    lista_type = Event_type.objects.all()  
    return render(request, '1.administrador/event_type.html', {
      'form':form,
      'lista_type':lista_type
    })
  else:
    form = Event_typeForm()

  lista_type = Event_type.objects.all()  

  return render(request, '1.administrador/event_type.html', {
    'form':form,
    'lista_type':lista_type
  })  

#  Agendar sesion fotografica
  
def agendar(request):
  if request.method == 'POST':
    form = SesionForm(request.POST)
    if form.is_valid():
      form.save()
      form = SesionForm()
    return render(request, '1.administrador/agendar.html', {
    'form':form,
    })
  else:
    form = SesionForm()
  return render(request, '1.administrador/agendar.html', {
  'form':form,
  })

# Listar sesiones 

def sesiones_list(request):
  lista_sesiones = Sesion.objects.all()
  return render(request, '1.administrador/lista_sesiones.html', {
    'lista_sesiones': lista_sesiones
  })

# Eliminar sesion 

def delete_sesion(request, id):
  eliminar = Sesion.objects.get(id=id)
  eliminar.delete()
  return redirect('lista_sesiones')

def delete_type(request, id):
  eliminar = Event_type.objects.get(id=id)
  eliminar.delete()
  return redirect('event_type')

def delete_status(request, id):
  eliminar = Status.objects.get(id=id)
  eliminar.delete()
  return redirect('crear_status')

# Editar sesion 

def edit_sesion(request, id):
  
  editarList = get_object_or_404(Sesion, id = id)

  if request.method == 'POST':
    form = SesionForm(request.POST, instance=editarList)
    if form.is_valid():
      form.save()

      # form = UsuarioForm(instance=editar)

    return redirect('lista_sesiones')
  
  else:

    form = SesionForm(instance=editarList)

  return render(request, '1.administrador/editar_sesion.html',{
      'form':form,
      'editarList':editarList
    }
    )
# en esta secion editamos los registros de pago 


# def delete_pago(request, id):
#   pago = Pagos.objects.get(id=id)
#   pago.delete()

#   return redirect('listar_pagos')

# def login_view(request):
#   if request.method == "POST":
#     email     = request.POST.get('email')
#     password  = request.POST.get('password')
#     # Verificar si email es de Admin o user
#     if Usuario.objects.filter(user_email=email).excists():
#       #Autentica como usuario
#       user  = authenticate(request, email=email,password=password)
#       if user:
#         login(request, user)
#         return redirect('usuario_dashboard')
#     elif Administrador.objects.filter(admin_email).excist():
#       admin = authenticate(request, email=email, password=password)
#       if admin:
#         login(request, admin)
#         return redirect('admin_dasboard')
    
#     context = {'error':'Email o contraseña incorrecta'}
#     return render(request, 'login.html', context)

#   else:
#     # en caso de que la solucitud sea GET
#     return render(request, 'login.html')
  
# @login_required
# def dashboard_view(request):
#     user = request.user  # El usuario autenticado
    
#     # Verificar si el usuario es administrador
#     if user.is_admin:
#         # Vista específica para el rol de administrador
#         context = {
#             'admin_info': 'Aquí muestra la información específica para los administradores.',
#             # Puedes incluir más información administrativa aquí
#         }
#         return render(request, 'admin_dashboard.html', context)
#     else:
#         # Vista específica para el rol de usuario
#         context = {
#             'user_info': 'Aquí muestra la información específica para los usuarios.',
#             # Puedes incluir más información de usuario aquí
#         }
#         return render(request, 'user_dashboard.html', context)