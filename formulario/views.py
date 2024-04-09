from django.shortcuts import render

# Create your views here.

def registrar(request):
  return render(request, 'registrar.html', {})