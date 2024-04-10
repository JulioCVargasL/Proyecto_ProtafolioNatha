from django.shortcuts import render
from django.http      import HttpResponse
from .models          import Pagos

# Create your views here.

def registrar(request):
  return render(request, 'registrar_pago.html', {})

#  metodo POST  y empleando un formulario
def registrar_pago(request):
  cotizacion   = request.POST['cotizacion']
  pay_comment  = request.POST['pay_comment']
  pay_status   = request.POST['pay_status']
  pay_date     = request.POST['pay_date']

  Pagos.objects.create(cotizacion=cotizacion, pay_comment=pay_comment, pay_status=pay_status, pay_date=pay_date)
  return  HttpResponse("Se registro el pago con exito")

def listar(request):
  pagos = Pagos.objects.all()

  return render(request, 'listar_pagos.html', {
    'pagos': pagos
  })