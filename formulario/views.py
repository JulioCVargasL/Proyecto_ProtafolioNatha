from django.shortcuts import render
from django.http      import HttpResponse
from .models          import Pagos

# Create your views here.

def registrar(request):
  return render(request, 'registrar.html', {})

#  metodo POST  y empleando un formulario
def registrar_pago(request):
  cotizacion   = request.GET['cotizacion']
  pay_comment  = request.GET['pay_comment']
  pay_status   = request.GET['pay_status']
  pay_date     = request.GET['pay_date']

  Pagos.objects.create(cotizacion=cotizacion, pay_comment=pay_comment, pay_status=pay_status, pay_date=pay_date)
  return  HttpResponse("Se registro el pago con exito")