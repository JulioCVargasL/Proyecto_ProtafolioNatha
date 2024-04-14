from django.shortcuts import render, redirect
from django.http      import HttpResponse
from .forms           import PagosForm
from .models          import Pagos


# Create your views here.



#  metodo POST  y empleando un formulario
def registrar_pago(request):
  if request.method == 'POST':
    form = PagosForm(request.POST)
    if form.is_valid():
      form.save()
      form = PagosForm()
      return render(request, 'registrar_pago.html', {
        'form':form,
      })
  else:
    form = PagosForm()
    return render(request, 'registrar_pago.html', {
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