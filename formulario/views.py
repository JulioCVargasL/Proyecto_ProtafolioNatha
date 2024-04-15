from django.shortcuts               import render, redirect
from django.http                    import HttpResponse
from .forms                         import PagosForm, StatusForm, SesionForm,LoginForm
from .models                        import Pagos,Usuario,Administrador
from django.contrib.auth.decorators import login_required

# Create your views here.

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


def crear_status(request):
  if request.method == 'POST':
    form = StatusForm(request.POST)
    if form.is_valid():
      form.save()
      form = StatusForm()
      return render(request, 'crear_status.html', {
        'form':form,
      })
  else:
    form = StatusForm()
    return render(request, 'crear_status.html', {
      'form':form,
    })

#  metodo POST  y empleando un formulario
def registrar_pago(request):
  if request.method == 'POST':
    form = PagosForm(request.POST)
    if form.is_valid():
      form.save()
      form = PagosForm()
      return render(request, 'registrar_pago.html', {
        'form':form,
        'success_message': 'Saved successfully!',
      })
  else:
    form = PagosForm()
    return render(request, 'registrar_pago.html', {
      'form':form,
    })
  
def agendar(request):
  if request.method == 'POST':
    form = SesionForm(request.POST)
    if form.is_valid():
      form.save()
      form = SesionForm()
      return render(request, 'agendar.html', {
        'form':form,
        'success_message': 'Saved successfully!',
      })
  else:
    form = PagosForm()
    return render(request, 'agendar.html', {
      'form':form,
    })

def listar(request):
  pagos = Pagos.objects.all()

  return render(request, 'listar_pagos.html', {
    'pagos': pagos
  })

def show_editar_pago(request):
  return render(request, 'editar_pagos.html', {})

# en esta secion editamos los registros de pago 
def editar_pago(request):
  id_pago      = request.POST['id_pago']
  cotizacion   = request.POST['cotizacion']
  pay_comment  = request.POST['pay_comment']
  pay_status   = request.POST['pay_status']
  pay_date     = request.POST['pay_date']

  editar       = Pagos.objects.get(id=id_pago)

  editar.cotizacion   = cotizacion
  editar.pay_comment  = pay_comment
  editar.pay_status   = pay_status
  editar.pay_date     = pay_date
  editar.save()

  return HttpResponse("Se ha editado con exito por formulario")

def delete_pago(request, id):
  pago = Pagos.objects.get(id=id)
  pago.delete()

  return redirect('listar_pagos')