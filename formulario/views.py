from django.shortcuts           import render, redirect
from django.http                import HttpResponse
from .forms                     import StatusForm,SesionForm,UsuarioForm,LoginForm,Event_typeForm
from .models                    import Usuario

def admin_dashboard(request):
  return render(request, '1.administrador/admin_dashboard.html')
# Create your views here.

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
  
def signup(request):
  if request.method == 'POST':
    form = UsuarioForm(request.POST)
    if form.is_valid():
      form.save()
      form = UsuarioForm()

    lista_usuarios = Usuario.objects.all()  
    return render(request, "registration/signup.html", {
      'form':form,
      'lista_usuarios':lista_usuarios
    })
  else:
    form = UsuarioForm()

  lista_usuarios = Usuario.objects.all()

  return render(request, 'registration/signup.html', {
    'form':form,
    'lista_usuarios':lista_usuarios
  })

# def user_list(request):
#   lista_usuarios = Usuario.objects.all()
#   return render(request, 'registration/signup.html', {
#     'lista_usuarios': lista_usuarios
#   })
  
def crear_status(request):
  if request.method == 'POST':
    form1 = StatusForm(request.POST, prefix='form1')
    if form1.is_valid():
      form1.save()
      
      form1 = StatusForm()
      
    return render(request, '1.administrador/crear_status.html', {
      'form1':form1
    })
    
  else:
    form1 = StatusForm(prefix='form1')
    
  return render(request, '1.administrador/crear_status.html', {
    'form':form1
  })
  
def event_type(request):
  if request.method == 'POST':
    form = Event_typeForm(request.POST)
    if form.is_valid():
      form.save()
      form = Event_typeForm()
    return render(request, '1.administrador/event_type.html', {
      'form':form,
    })
  else:
    form = Event_typeForm()
  return render(request, '1.administrador/event_type.html', {
    'form':form,
  })  

#  metodo POST  y empleando un formulario
  
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