from rest_framework import serializers
from .models import Mascotas
from .models import Alimentos
from .models import Accesorios
class MascotasSerializable(serializers.ModelSerializer):
  class Meta:
    model=Mascotas
    fields=(
      'nombre',
      'raza',
      'edad',
      'sexo',
    )
class AlimentosSerializable(serializers.ModelSerializer):    
  class Meta:
    model=Alimentos
    fields=(
      'codigo',
      'tipo_alimento',
      'marca',
      'cantidad',
      'precio',
    )
class AccesoriosSerializable(serializers.ModelSerializer):    
  class Meta:
    model=Accesorios
    fields=(
      'marca',
      'nombre',
      'codigo',
      'color',
      'tamaño',
    )