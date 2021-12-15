from django.shortcuts import render
from rest_framework import viewsets
from .models import Mascotas
from .models import Alimentos
from .models import Accesorios
from .serializers import MascotasSerializable
from .serializers import AlimentosSerializable
from .serializers import AccesoriosSerializable

# Create your views here.
class MascotasVista(viewsets.ModelViewSet):
  serializer_class:MascotasSerializable
  queryset=Mascotas.objects.all();
class AlimentosVista(viewsets.ModelViewSet):
  serializer_class:AlimentosSerializable
  queryset=Alimentos.objects.all();
class AccesoriosVista(viewsets.ModelViewSet):
  serializer_class:AccesoriosSerializable
  queryset=Accesorios.objects.all();

  
